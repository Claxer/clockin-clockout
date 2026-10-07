import sqlite3
from pathlib import Path
from datetime import datetime, date


DB_FILE = Path(__file__).with_name("attendance.db")


def get_connection():
    connection = sqlite3.connect(DB_FILE)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def create_tables():
    with get_connection() as connection:
        connection.executescript("""
        CREATE TABLE IF NOT EXISTS employees (
            employee_id TEXT PRIMARY KEY,
            full_name TEXT NOT NULL,
            department TEXT NOT NULL,
            position TEXT NOT NULL,
            email TEXT DEFAULT '',
            phone TEXT DEFAULT '',
            date_hired TEXT DEFAULT '',
            status TEXT NOT NULL DEFAULT 'Active',
            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT NOT NULL,
            work_date TEXT NOT NULL,
            clock_in TEXT NOT NULL,
            clock_out TEXT,
            total_hours REAL DEFAULT 0,
            status TEXT NOT NULL DEFAULT 'Present',
            notes TEXT DEFAULT '',
            FOREIGN KEY (employee_id)
                REFERENCES employees(employee_id)
                ON DELETE CASCADE
        );

        CREATE INDEX IF NOT EXISTS idx_attendance_date
        ON attendance(work_date);

        CREATE INDEX IF NOT EXISTS idx_attendance_employee
        ON attendance(employee_id);
        """)


def add_employee(
    employee_id,
    full_name,
    department,
    position,
    email="",
    phone="",
    date_hired=""
):
    with get_connection() as connection:
        connection.execute("""
            INSERT INTO employees
            (
                employee_id,
                full_name,
                department,
                position,
                email,
                phone,
                date_hired,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            employee_id.strip(),
            full_name.strip(),
            department.strip(),
            position.strip(),
            email.strip(),
            phone.strip(),
            date_hired.strip(),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))


def update_employee(
    employee_id,
    full_name,
    department,
    position,
    email="",
    phone="",
    date_hired="",
    status="Active"
):
    with get_connection() as connection:
        connection.execute("""
            UPDATE employees
            SET
                full_name=?,
                department=?,
                position=?,
                email=?,
                phone=?,
                date_hired=?,
                status=?
            WHERE employee_id=?
        """, (
            full_name.strip(),
            department.strip(),
            position.strip(),
            email.strip(),
            phone.strip(),
            date_hired.strip(),
            status,
            employee_id
        ))


def delete_employee(employee_id):
    with get_connection() as connection:
        connection.execute(
            "DELETE FROM employees WHERE employee_id=?",
            (employee_id,)
        )


def get_employees(search=""):
    with get_connection() as connection:
        if search.strip():
            value = f"%{search.strip()}%"

            return connection.execute("""
                SELECT *
                FROM employees
                WHERE employee_id LIKE ?
                   OR full_name LIKE ?
                   OR department LIKE ?
                   OR position LIKE ?
                ORDER BY full_name
            """, (
                value,
                value,
                value,
                value
            )).fetchall()

        return connection.execute("""
            SELECT *
            FROM employees
            ORDER BY full_name
        """).fetchall()


def get_employee(employee_id):
    with get_connection() as connection:
        return connection.execute("""
            SELECT *
            FROM employees
            WHERE employee_id=?
        """, (employee_id,)).fetchone()


def clock_in(employee_id):
    today = date.today().isoformat()
    now = datetime.now().strftime("%H:%M:%S")

    with get_connection() as connection:
        existing = connection.execute("""
            SELECT id, clock_out
            FROM attendance
            WHERE employee_id=?
              AND work_date=?
            ORDER BY id DESC
            LIMIT 1
        """, (
            employee_id,
            today
        )).fetchone()

        if existing and existing["clock_out"] is None:
            return False, "Employee is already clocked in."

        connection.execute("""
            INSERT INTO attendance
            (
                employee_id,
                work_date,
                clock_in,
                status
            )
            VALUES (?, ?, ?, 'Present')
        """, (
            employee_id,
            today,
            now
        ))

    return True, f"Clocked in at {now}."


def clock_out(employee_id):
    today = date.today().isoformat()
    now = datetime.now().strftime("%H:%M:%S")

    with get_connection() as connection:
        row = connection.execute("""
            SELECT id, clock_in
            FROM attendance
            WHERE employee_id=?
              AND work_date=?
              AND clock_out IS NULL
            ORDER BY id DESC
            LIMIT 1
        """, (
            employee_id,
            today
        )).fetchone()

        if not row:
            return False, "Employee is not currently clocked in."

        start = datetime.strptime(
            row["clock_in"],
            "%H:%M:%S"
        )

        end = datetime.strptime(
            now,
            "%H:%M:%S"
        )

        hours = max(
            0,
            (end - start).total_seconds() / 3600
        )

        connection.execute("""
            UPDATE attendance
            SET
                clock_out=?,
                total_hours=?
            WHERE id=?
        """, (
            now,
            round(hours, 2),
            row["id"]
        ))

    return True, f"Clocked out at {now}. Total hours: {hours:.2f}"


def get_attendance(
    search="",
    start_date="",
    end_date=""
):
    query = """
        SELECT
            a.id,
            a.employee_id,
            e.full_name,
            e.department,
            e.position,
            a.work_date,
            a.clock_in,
            a.clock_out,
            a.total_hours,
            a.status,
            a.notes
        FROM attendance a
        JOIN employees e
            ON e.employee_id = a.employee_id
        WHERE 1=1
    """

    params = []

    if search.strip():
        value = f"%{search.strip()}%"

        query += """
            AND (
                a.employee_id LIKE ?
                OR e.full_name LIKE ?
                OR e.department LIKE ?
            )
        """

        params.extend([
            value,
            value,
            value
        ])

    if start_date:
        query += " AND a.work_date >= ?"
        params.append(start_date)

    if end_date:
        query += " AND a.work_date <= ?"
        params.append(end_date)

    query += """
        ORDER BY
            a.work_date DESC,
            a.clock_in DESC
    """

    with get_connection() as connection:
        return connection.execute(
            query,
            params
        ).fetchall()


def get_today_attendance():
    today = date.today().isoformat()

    return get_attendance(
        start_date=today,
        end_date=today
    )


def get_dashboard_stats():
    today = date.today().isoformat()

    with get_connection() as connection:

        employees = connection.execute("""
            SELECT COUNT(*) AS total
            FROM employees
            WHERE status='Active'
        """).fetchone()["total"]

        present = connection.execute("""
            SELECT COUNT(*) AS total
            FROM attendance
            WHERE work_date=?
        """, (today,)).fetchone()["total"]

        working = connection.execute("""
            SELECT COUNT(*) AS total
            FROM attendance
            WHERE work_date=?
              AND clock_out IS NULL
        """, (today,)).fetchone()["total"]

        hours = connection.execute("""
            SELECT COALESCE(SUM(total_hours), 0) AS total
            FROM attendance
            WHERE work_date=?
        """, (today,)).fetchone()["total"]

    return {
        "employees": employees,
        "present": present,
        "working": working,
        "hours": round(hours, 2)
    }


def get_report_summary(start_date, end_date):
    with get_connection() as connection:

        summary = connection.execute("""
            SELECT
                COUNT(*) AS total_records,
                COUNT(DISTINCT employee_id) AS unique_employees,
                COALESCE(SUM(total_hours), 0) AS total_hours,
                COALESCE(AVG(total_hours), 0) AS average_hours
            FROM attendance
            WHERE work_date BETWEEN ? AND ?
        """, (
            start_date,
            end_date
        )).fetchone()

        departments = connection.execute("""
            SELECT
                e.department,
                COUNT(a.id) AS attendance_count,
                COALESCE(SUM(a.total_hours), 0) AS total_hours
            FROM attendance a
            JOIN employees e
                ON e.employee_id = a.employee_id
            WHERE a.work_date BETWEEN ? AND ?
            GROUP BY e.department
            ORDER BY attendance_count DESC
        """, (
            start_date,
            end_date
        )).fetchall()

    return summary, departments
