import sqlite3


DATABASE_NAME = "company_attnce.db"


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():
    return sqlite3.connect(DATABASE_NAME)


# ============================================================
# CREATE DATABASE TABLES
# ============================================================

def create_tables():

    connection = get_connection()
    cursor = connection.cursor()

    # --------------------------------------------------------
    # EMPLOYEES TABLE
    # --------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            position TEXT NOT NULL
        )
    """)

    # --------------------------------------------------------
    # ATTENDANCE TABLE
    # --------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT NOT NULL,
            employee_name TEXT NOT NULL,
            clock_in TEXT NOT NULL,
            clock_out TEXT,
            total_hours TEXT
        )
    """)

    connection.commit()
    connection.close()


# ============================================================
# EMPLOYEE FUNCTIONS
# ============================================================

def add_employee(
    employee_id,
    name,
    department,
    position
):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute("""
            INSERT INTO employees
            (
                employee_id,
                name,
                department,
                position
            )
            VALUES (?, ?, ?, ?)
        """, (
            employee_id,
            name,
            department,
            position
        ))

        connection.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        connection.close()


def get_all_employees():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            employee_id,
            name,
            department,
            position
        FROM employees
        ORDER BY name
    """)

    employees = cursor.fetchall()

    connection.close()

    return employees


def get_employee(employee_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            employee_id,
            name,
            department,
            position
        FROM employees
        WHERE employee_id = ?
    """, (employee_id,))

    employee = cursor.fetchone()

    connection.close()

    return employee


def delete_employee(employee_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM employees
        WHERE employee_id = ?
    """, (employee_id,))

    connection.commit()

    connection.close()


def search_employees(search_text):

    connection = get_connection()
    cursor = connection.cursor()

    search_value = f"%{search_text}%"

    cursor.execute("""
        SELECT
            employee_id,
            name,
            department,
            position
        FROM employees
        WHERE employee_id LIKE ?
           OR name LIKE ?
           OR department LIKE ?
           OR position LIKE ?
        ORDER BY name
    """, (
        search_value,
        search_value,
        search_value,
        search_value
    ))

    employees = cursor.fetchall()

    connection.close()

    return employees


# ============================================================
# ATTENDANCE FUNCTIONS
# ============================================================

def add_attendance(
    employee_id,
    employee_name,
    clock_in
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO attendance
        (
            employee_id,
            employee_name,
            clock_in
        )
        VALUES (?, ?, ?)
    """, (
        employee_id,
        employee_name,
        clock_in
    ))

    connection.commit()

    connection.close()


def get_active_attendance(employee_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            employee_id,
            employee_name,
            clock_in
        FROM attendance
        WHERE employee_id = ?
        AND clock_out IS NULL
        ORDER BY id DESC
        LIMIT 1
    """, (employee_id,))

    attendance = cursor.fetchone()

    connection.close()

    return attendance


def clock_out_employee(
    attendance_id,
    clock_out,
    total_hours
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE attendance
        SET
            clock_out = ?,
            total_hours = ?
        WHERE id = ?
    """, (
        clock_out,
        total_hours,
        attendance_id
    ))

    connection.commit()

    connection.close()


def get_all_attendance():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            employee_id,
            employee_name,
            clock_in,
            clock_out,
            total_hours
        FROM attendance
        ORDER BY id DESC
    """)

    attendance = cursor.fetchall()

    connection.close()

    return attendance


def get_today_attendance():

    connection = get_connection()
    cursor = connection.cursor()

    today = __import__("datetime").datetime.now().strftime(
        "%Y-%m-%d"
    )

    cursor.execute("""
        SELECT
            employee_id,
            employee_name,
            clock_in,
            clock_out,
            total_hours
        FROM attendance
        WHERE clock_in LIKE ?
        ORDER BY id DESC
    """, (today + "%",))

    attendance = cursor.fetchall()

    connection.close()

    return attendance


# ============================================================
# SEARCH ATTENDANCE
# ============================================================

def search_attendance(search_text):

    connection = get_connection()
    cursor = connection.cursor()

    search_value = f"%{search_text}%"

    cursor.execute("""
        SELECT
            employee_id,
            employee_name,
            clock_in,
            clock_out,
            total_hours
        FROM attendance
        WHERE employee_id LIKE ?
           OR employee_name LIKE ?
        ORDER BY id DESC
    """, (
        search_value,
        search_value
    ))

    attendance = cursor.fetchall()

    connection.close()

    return attendance


# ============================================================
# DASHBOARD STATISTICS
# ============================================================

def get_employee_count():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM employees
    """)

    count = cursor.fetchone()[0]

    connection.close()

    return count


def get_clocked_in_count():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM attendance
        WHERE clock_out IS NULL
    """)

    count = cursor.fetchone()[0]

    connection.close()

    return count


def get_clocked_out_count():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM attendance
        WHERE clock_out IS NOT NULL
    """)

    count = cursor.fetchone()[0]

    connection.close()

    return count
