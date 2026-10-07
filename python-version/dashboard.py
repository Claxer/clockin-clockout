import customtkinter as ctk
from datetime import datetime
import database


def show_dashboard(parent):
    # Main dashboard frame
    dashboard_frame = ctk.CTkFrame(
        parent,
        fg_color="#f5f5f5",
        corner_radius=0
    )
    dashboard_frame.pack(fill="both", expand=True)

    # Header
    header_frame = ctk.CTkFrame(
        dashboard_frame,
        fg_color="transparent"
    )
    header_frame.pack(
        fill="x",
        padx=30,
        pady=(25, 10)
    )

    title = ctk.CTkLabel(
        header_frame,
        text="Dashboard",
        font=ctk.CTkFont(size=30, weight="bold"),
        text_color="#222222"
    )
    title.pack(side="left")

    date_label = ctk.CTkLabel(
        header_frame,
        text=datetime.now().strftime("%B %d, %Y"),
        font=ctk.CTkFont(size=15),
        text_color="#666666"
    )
    date_label.pack(side="right", pady=8)

    # Get statistics
    total_employees = get_total_employees()
    present_today = get_present_today()
    late_today = get_late_today()

    absent_today = total_employees - present_today

    if absent_today < 0:
        absent_today = 0

    # Statistics container
    stats_frame = ctk.CTkFrame(
        dashboard_frame,
        fg_color="transparent"
    )
    stats_frame.pack(
        fill="x",
        padx=30,
        pady=15
    )

    # Statistics cards
    create_stat_card(
        stats_frame,
        "Total Employees",
        str(total_employees),
        0
    )

    create_stat_card(
        stats_frame,
        "Present Today",
        str(present_today),
        1
    )

    create_stat_card(
        stats_frame,
        "Late Today",
        str(late_today),
        2
    )

    create_stat_card(
        stats_frame,
        "Absent Today",
        str(absent_today),
        3
    )

    # Recent attendance section
    recent_frame = ctk.CTkFrame(
        dashboard_frame,
        fg_color="white",
        corner_radius=12
    )
    recent_frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=(10, 25)
    )

    recent_title = ctk.CTkLabel(
        recent_frame,
        text="Recent Attendance",
        font=ctk.CTkFont(size=20, weight="bold"),
        text_color="#222222"
    )
    recent_title.pack(
        anchor="w",
        padx=20,
        pady=(20, 10)
    )

    # Scrollable area
    records_frame = ctk.CTkScrollableFrame(
        recent_frame,
        fg_color="white"
    )
    records_frame.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=(0, 15)
    )

    show_recent_attendance(records_frame)


def create_stat_card(parent, title, value, column):
    card = ctk.CTkFrame(
        parent,
        fg_color="white",
        corner_radius=12,
        height=120
    )

    card.grid(
        row=0,
        column=column,
        padx=6,
        sticky="nsew"
    )

    parent.grid_columnconfigure(
        column,
        weight=1
    )

    title_label = ctk.CTkLabel(
        card,
        text=title,
        font=ctk.CTkFont(size=14),
        text_color="#777777"
    )
    title_label.pack(
        anchor="w",
        padx=18,
        pady=(18, 3)
    )

    value_label = ctk.CTkLabel(
        card,
        text=value,
        font=ctk.CTkFont(size=28, weight="bold"),
        text_color="#222222"
    )
    value_label.pack(
        anchor="w",
        padx=18
    )


def get_total_employees():
    try:
        connection = database.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM employees"
        )

        result = cursor.fetchone()

        connection.close()

        return result[0]

    except Exception:
        return 0


def get_present_today():
    try:
        connection = database.get_connection()
        cursor = connection.cursor()

        today = datetime.now().strftime("%Y-%m-%d")

        cursor.execute(
            """
            SELECT COUNT(DISTINCT employee_id)
            FROM attendance
            WHERE date = ?
            AND time_in IS NOT NULL
            """,
            (today,)
        )

        result = cursor.fetchone()

        connection.close()

        return result[0]

    except Exception:
        return 0


def get_late_today():
    try:
        connection = database.get_connection()
        cursor = connection.cursor()

        today = datetime.now().strftime("%Y-%m-%d")

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM attendance
            WHERE date = ?
            AND status = 'Late'
            """,
            (today,)
        )

        result = cursor.fetchone()

        connection.close()

        return result[0]

    except Exception:
        return 0


def show_recent_attendance(parent):
    try:
        connection = database.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                employees.name,
                attendance.date,
                attendance.time_in,
                attendance.time_out,
                attendance.status
            FROM attendance
            JOIN employees
            ON attendance.employee_id = employees.id
            ORDER BY attendance.id DESC
            LIMIT 10
            """
        )

        records = cursor.fetchall()

        connection.close()

        # Table header
        create_header(parent, "Employee", 0)
        create_header(parent, "Date", 1)
        create_header(parent, "Time In", 2)
        create_header(parent, "Time Out", 3)
        create_header(parent, "Status", 4)

        for row, record in enumerate(records, start=1):
            name = record[0]
            date = record[1]
            time_in = record[2]
            time_out = record[3]
            status = record[4]

            create_cell(parent, name, row, 0)
            create_cell(parent, date, row, 1)
            create_cell(parent, time_in or "-", row, 2)
            create_cell(parent, time_out or "-", row, 3)
            create_cell(parent, status or "-", row, 4)

        if not records:
            empty_label = ctk.CTkLabel(
                parent,
                text="No attendance records yet.",
                font=ctk.CTkFont(size=14),
                text_color="#777777"
            )
            empty_label.grid(
                row=1,
                column=0,
                columnspan=5,
                pady=30
            )

    except Exception as error:
        error_label = ctk.CTkLabel(
            parent,
            text="Unable to load attendance records.",
            font=ctk.CTkFont(size=14),
            text_color="#777777"
        )
        error_label.pack(pady=30)


def create_header(parent, text, column):
    label = ctk.CTkLabel(
        parent,
        text=text,
        font=ctk.CTkFont(size=13, weight="bold"),
        text_color="#555555"
    )

    label.grid(
        row=0,
        column=column,
        padx=10,
        pady=10,
        sticky="w"
    )

    parent.grid_columnconfigure(
        column,
        weight=1
    )


def create_cell(parent, text, row, column):
    label = ctk.CTkLabel(
        parent,
        text=str(text),
        font=ctk.CTkFont(size=13),
        text_color="#333333"
    )

    label.grid(
        row=row,
        column=column,
        padx=10,
        pady=8,
        sticky="w"
    )
