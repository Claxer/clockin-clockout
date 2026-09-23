import sqlite3
from datetime import datetime

DATABASE_NAME = "company_attendance.db"


def connect_db():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def create_tables():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            position TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT NOT NULL,
            date TEXT NOT NULL,
            clock_in TEXT,
            clock_out TEXT,
            total_hours REAL DEFAULT 0,
            overtime_hours REAL DEFAULT 0,
            status TEXT DEFAULT 'Present',
            remarks TEXT DEFAULT ''
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            setting_name TEXT UNIQUE NOT NULL,
            setting_value TEXT
        )
    """)

    # Add new columns to older databases if they do not exist
    add_column_if_missing(
        cursor,
        "attendance",
        "overtime_hours",
        "REAL DEFAULT 0"
    )

    add_column_if_missing(
        cursor,
        "attendance",
        "status",
        "TEXT DEFAULT 'Present'"
    )

    add_column_if_missing(
        cursor,
        "attendance",
        "remarks",
        "TEXT DEFAULT ''"
    )

    connection.commit()
    connection.close()


def add_column_if_missing(cursor, table_name, column_name, column_definition):
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [row[1] for row in cursor.fetchall()]

    if column_name not in columns:
        cursor.execute(
            f"ALTER TABLE {table_name} "
            f"ADD COLUMN {column_name} {column_definition}"
        )


# =========================================================
# EMPLOYEE FUNCTIONS
# =========================================================

def add_employee(employee_id, name, department, position):
    connection = connect_db()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO employees
            (employee_id, name, department, position)
            VALUES (?, ?, ?, ?)
        """, (
            employee_id,
            name,
            department,
            position
        ))

        connection.commit()
        return True, "Employee added successfully."

    except sqlite3.IntegrityError:
        return False, "Employee ID already exists."

    finally:
        connection.close()


def update_employee(employee_id, name, department, position):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE employees
        SET name = ?,
            department = ?,
            position = ?
        WHERE employee_id = ?
    """, (
        name,
        department,
        position,
        employee_id
    ))

    connection.commit()
    changed = cursor.rowcount > 0
    connection.close()

    return changed


def delete_employee(employee_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM employees
        WHERE employee_id = ?
    """, (employee_id,))

    connection.commit()
    changed = cursor.rowcount > 0
    connection.close()

    return changed


def get_employee(employee_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM employees
        WHERE employee_id = ?
    """, (employee_id,))

    employee = cursor.fetchone()
    connection.close()

    return employee


def get_all_employees(search=""):
    connection = connect_db()
    cursor = connection.cursor()

    if search:
        cursor.execute("""
            SELECT *
            FROM employees
            WHERE employee_id LIKE ?
               OR name LIKE ?
               OR department LIKE ?
               OR position LIKE ?
            ORDER BY name
        """, (
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        ))
    else:
        cursor.execute("""
            SELECT *
            FROM employees
            ORDER BY name
        """)

    employees = cursor.fetchall()
    connection.close()

    return employees


# =========================================================
# ATTENDANCE FUNCTIONS
# =========================================================

def get_active_attendance(employee_id):
    connection = connect_db()
    cursor = connection.cursor()

    today = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        SELECT *
        FROM attendance
        WHERE employee_id = ?
          AND date = ?
          AND clock_out IS NULL
        ORDER BY id DESC
        LIMIT 1
    """, (
        employee_id,
        today
    ))

    record = cursor.fetchone()
    connection.close()

    return record


def clock_employee_in(employee_id):
    employee = get_employee(employee_id)

    if not employee:
        return False, "Employee not found."

    if get_active_attendance(employee_id):
        return False, f"{employee['name']} is already clocked in."

    connection = connect_db()
    cursor = connection.cursor()

    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")

    # 9:00 AM is used as the default shift start time
    shift_start = now.replace(
        hour=9,
        minute=0,
        second=0,
        microsecond=0
    )

    if now > shift_start:
        status = "Late"
        minutes_late = int(
            (now - shift_start).total_seconds() / 60
        )
        remarks = f"{minutes_late} minute(s) late"
    else:
        status = "Present"
        remarks = "On time"

    cursor.execute("""
        INSERT INTO attendance
        (
            employee_id,
            date,
            clock_in,
            status,
            remarks
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        employee_id,
        today,
        current_time,
        status,
        remarks
    ))

    connection.commit()
    connection.close()

    return True, f"{employee['name']} clocked in successfully."


def clock_employee_out(employee_id):
    employee = get_employee(employee_id)

    if not employee:
        return False, "Employee not found.", 0

    record = get_active_attendance(employee_id)

    if not record:
        return False, f"{employee['name']} is not clocked in.", 0

    now = datetime.now()

    clock_in_datetime = datetime.strptime(
        f"{record['date']} {record['clock_in']}",
        "%Y-%m-%d %H:%M:%S"
    )

    difference = now - clock_in_datetime

    total_hours = difference.total_seconds() / 3600

    overtime_hours = max(
        0,
        total_hours - 8
    )

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE attendance
        SET clock_out = ?,
            total_hours = ?,
            overtime_hours = ?
        WHERE id = ?
    """, (
        now.strftime("%H:%M:%S"),
        round(total_hours, 2),
        round(overtime_hours, 2),
        record["id"]
    ))

    connection.commit()
    connection.close()

    return (
        True,
        f"{employee['name']} clocked out successfully.",
        round(total_hours, 2)
    )


def get_attendance(search="", selected_date="", status="All"):
    connection = connect_db()
    cursor = connection.cursor()

    query = """
        SELECT
            attendance.id,
            attendance.employee_id,
            employees.name,
            employees.department,
            employees.position,
            attendance.date,
            attendance.clock_in,
            attendance.clock_out,
            attendance.total_hours,
            attendance.overtime_hours,
            attendance.status,
            attendance.remarks
        FROM attendance
        JOIN employees
        ON attendance.employee_id = employees.employee_id
        WHERE 1 = 1
    """

    parameters = []

    if search:
        query += """
            AND (
                attendance.employee_id LIKE ?
                OR employees.name LIKE ?
                OR employees.department LIKE ?
            )
        """

        search_value = f"%{search}%"

        parameters.extend([
            search_value,
            search_value,
            search_value
        ])

    if selected_date:
        query += " AND attendance.date = ?"
        parameters.append(selected_date)

    if status != "All":
        query += " AND attendance.status = ?"
        parameters.append(status)

    query += " ORDER BY attendance.id DESC"

    cursor.execute(
        query,
        parameters
    )

    records = cursor.fetchall()
    connection.close()

    return records


def get_today_attendance():
    today = datetime.now().strftime("%Y-%m-%d")

    return get_attendance(
        selected_date=today
    )


# =========================================================
# DASHBOARD STATISTICS
# =========================================================

def get_dashboard_stats():
    connection = connect_db()
    cursor = connection.cursor()

    today = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        SELECT COUNT(*)
        FROM employees
    """)

    total_employees = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM attendance
        WHERE date = ?
          AND clock_out IS NULL
    """, (today,))

    currently_working = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM attendance
        WHERE date = ?
    """, (today,))

    today_records = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM attendance
        WHERE date = ?
          AND clock_out IS NOT NULL
    """, (today,))

    completed = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COALESCE(SUM(total_hours), 0)
        FROM attendance
        WHERE date = ?
    """, (today,))

    total_hours = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM attendance
        WHERE date = ?
          AND status = 'Late'
    """, (today,))

    late_count = cursor.fetchone()[0]

    connection.close()

    return {
        "total_employees": total_employees,
        "currently_working": currently_working,
        "today_records": today_records,
        "completed": completed,
        "total_hours": total_hours,
        "late_count": late_count
    }


# =========================================================
# REPORT FUNCTIONS
# =========================================================

def get_employee_summary(employee_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            COUNT(*) AS total_days,
            COALESCE(SUM(total_hours), 0) AS total_hours,
            COALESCE(SUM(overtime_hours), 0) AS overtime_hours,
            COALESCE(
                SUM(
                    CASE
                        WHEN status = 'Late'
                        THEN 1
                        ELSE 0
                    END
                ),
                0
            ) AS late_count
        FROM attendance
        WHERE employee_id = ?
    """, (employee_id,))

    result = cursor.fetchone()
    connection.close()

    return result


def get_monthly_summary(year, month):
    connection = connect_db()
    cursor = connection.cursor()

    month_text = f"{year}-{month:02d}"

    cursor.execute("""
        SELECT
            COUNT(*) AS total_records,
            COALESCE(SUM(total_hours), 0) AS total_hours,
            COALESCE(SUM(overtime_hours), 0) AS overtime_hours
        FROM attendance
        WHERE date LIKE ?
    """, (f"{month_text}-%",))

    result = cursor.fetchone()
    connection.close()

    return result
