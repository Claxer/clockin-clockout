import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
import database


def show_attendance(parent):
    attendance_frame = ctk.CTkFrame(
        parent,
        fg_color="#f5f5f5",
        corner_radius=0
    )
    attendance_frame.pack(
        fill="both",
        expand=True
    )

    # Header
    header_frame = ctk.CTkFrame(
        attendance_frame,
        fg_color="transparent"
    )
    header_frame.pack(
        fill="x",
        padx=30,
        pady=(25, 15)
    )

    title = ctk.CTkLabel(
        header_frame,
        text="Attendance",
        font=ctk.CTkFont(
            size=30,
            weight="bold"
        ),
        text_color="#222222"
    )
    title.pack(side="left")

    date_label = ctk.CTkLabel(
        header_frame,
        text=datetime.now().strftime("%B %d, %Y"),
        font=ctk.CTkFont(size=15),
        text_color="#666666"
    )
    date_label.pack(
        side="right",
        pady=8
    )

    # Clock in / Clock out section
    action_frame = ctk.CTkFrame(
        attendance_frame,
        fg_color="white",
        corner_radius=12
    )
    action_frame.pack(
        fill="x",
        padx=30,
        pady=(5, 15)
    )

    action_title = ctk.CTkLabel(
        action_frame,
        text="Employee Time Tracking",
        font=ctk.CTkFont(
            size=20,
            weight="bold"
        ),
        text_color="#222222"
    )
    action_title.pack(
        anchor="w",
        padx=25,
        pady=(20, 15)
    )

    employee_frame = ctk.CTkFrame(
        action_frame,
        fg_color="transparent"
    )
    employee_frame.pack(
        fill="x",
        padx=25,
        pady=(0, 20)
    )

    employee_list = get_employees()

    employee_names = []

    for employee in employee_list:
        employee_names.append(
            f"{employee[0]} - {employee[1]}"
        )

    if employee_names:
        employee_dropdown = ctk.CTkComboBox(
            employee_frame,
            values=employee_names,
            width=350,
            height=40
        )
        employee_dropdown.set(
            "Select Employee"
        )
    else:
        employee_dropdown = ctk.CTkComboBox(
            employee_frame,
            values=["No employees available"],
            width=350,
            height=40
        )
        employee_dropdown.set(
            "No employees available"
        )

    employee_dropdown.pack(
        side="left",
        padx=(0, 10)
    )

    clock_in_button = ctk.CTkButton(
        employee_frame,
        text="Clock In",
        width=120,
        height=40,
        command=lambda: clock_in(
            employee_dropdown,
            parent
        )
    )
    clock_in_button.pack(
        side="left",
        padx=5
    )

    clock_out_button = ctk.CTkButton(
        employee_frame,
        text="Clock Out",
        width=120,
        height=40,
        fg_color="#555555",
        hover_color="#444444",
        command=lambda: clock_out(
            employee_dropdown,
            parent
        )
    )
    clock_out_button.pack(
        side="left",
        padx=5
    )

    # Today's attendance
    records_frame = ctk.CTkFrame(
        attendance_frame,
        fg_color="white",
        corner_radius=12
    )
    records_frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=(0, 25)
    )

    records_title = ctk.CTkLabel(
        records_frame,
        text="Today's Attendance",
        font=ctk.CTkFont(
            size=20,
            weight="bold"
        ),
        text_color="#222222"
    )
    records_title.pack(
        anchor="w",
        padx=20,
        pady=(20, 10)
    )

    table_frame = ctk.CTkScrollableFrame(
        records_frame,
        fg_color="white"
    )
    table_frame.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=(0, 10)
    )

    load_today_attendance(table_frame)


def get_employees():
    try:
        connection = database.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id, name
            FROM employees
            ORDER BY name
            """
        )

        employees = cursor.fetchall()

        connection.close()

        return employees

    except Exception:
        return []


def get_employee_id(employee_dropdown):
    selected = employee_dropdown.get()

    if not selected or selected in [
        "Select Employee",
        "No employees available"
    ]:
        return None

    try:
        employee_id = selected.split(" - ")[0]
        return int(employee_id)

    except ValueError:
        return None


def clock_in(employee_dropdown, parent):
    employee_id = get_employee_id(
        employee_dropdown
    )

    if employee_id is None:
        messagebox.showwarning(
            "Select Employee",
            "Please select an employee first."
        )
        return

    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    try:
        connection = database.get_connection()
        cursor = connection.cursor()

        # Check if employee already clocked in today
        cursor.execute(
            """
            SELECT id
            FROM attendance
            WHERE employee_id = ?
            AND date = ?
            """,
            (
                employee_id,
                today
            )
        )

        existing_record = cursor.fetchone()

        if existing_record:
            connection.close()

            messagebox.showwarning(
                "Already Clocked In",
                "This employee already has an attendance record today."
            )
            return

        # Determine attendance status
        current_hour = datetime.now().hour
        current_minute = datetime.now().minute

        if current_hour > 8 or (
            current_hour == 8 and current_minute > 0
        ):
            status = "Late"
        else:
            status = "Present"

        cursor.execute(
            """
            INSERT INTO attendance
            (employee_id, date, time_in, time_out, status)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                employee_id,
                today,
                current_time,
                None,
                status
            )
        )

        connection.commit()
        connection.close()

        messagebox.showinfo(
            "Clock In Successful",
            "Employee successfully clocked in."
        )

        show_attendance(parent)

    except Exception as error:
        messagebox.showerror(
            "Database Error",
            str(error)
        )


def clock_out(employee_dropdown, parent):
    employee_id = get_employee_id(
        employee_dropdown
    )

    if employee_id is None:
        messagebox.showwarning(
            "Select Employee",
            "Please select an employee first."
        )
        return

    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    try:
        connection = database.get_connection()
        cursor = connection.cursor()

        # Find today's attendance record
        cursor.execute(
            """
            SELECT id, time_out
            FROM attendance
            WHERE employee_id = ?
            AND date = ?
            """,
            (
                employee_id,
                today
            )
        )

        record = cursor.fetchone()

        if not record:
            connection.close()

            messagebox.showwarning(
                "No Clock In",
                "This employee has not clocked in today."
            )
            return

        if record[1]:
            connection.close()

            messagebox.showwarning(
                "Already Clocked Out",
                "This employee has already clocked out today."
            )
            return

        cursor.execute(
            """
            UPDATE attendance
            SET time_out = ?
            WHERE id = ?
            """,
            (
                current_time,
                record[0]
            )
        )

        connection.commit()
        connection.close()

        messagebox.showinfo(
            "Clock Out Successful",
            "Employee successfully clocked out."
        )

        show_attendance(parent)

    except Exception as error:
        messagebox.showerror(
            "Database Error",
            str(error)
        )


def load_today_attendance(parent):
    # Clear existing widgets
    for widget in parent.winfo_children():
        widget.destroy()

    try:
        connection = database.get_connection()
        cursor = connection.cursor()

        today = datetime.now().strftime("%Y-%m-%d")

        cursor.execute(
            """
            SELECT
                attendance.id,
                employees.name,
                attendance.date,
                attendance.time_in,
                attendance.time_out,
                attendance.status
            FROM attendance
            JOIN employees
            ON attendance.employee_id = employees.id
            WHERE attendance.date = ?
            ORDER BY attendance.id DESC
            """,
            (today,)
        )

        records = cursor.fetchall()

        connection.close()

        headers = [
            "ID",
            "Employee",
            "Date",
            "Time In",
            "Time Out",
            "Status"
        ]

        for column, header in enumerate(headers):
            label = ctk.CTkLabel(
                parent,
                text=header,
                font=ctk.CTkFont(
                    size=13,
                    weight="bold"
                ),
                text_color="#555555"
            )

            label.grid(
                row=0,
                column=column,
                padx=10,
                pady=12,
                sticky="w"
            )

            parent.grid_columnconfigure(
                column,
                weight=1
            )

        for row, record in enumerate(
            records,
            start=1
        ):
            create_cell(
                parent,
                record[0],
                row,
                0
            )

            create_cell(
                parent,
                record[1],
                row,
                1
            )

            create_cell(
                parent,
                record[2],
                row,
                2
            )

            create_cell(
                parent,
                record[3] or "-",
                row,
                3
            )

            create_cell(
                parent,
                record[4] or "-",
                row,
                4
            )

            create_cell(
                parent,
                record[5],
                row,
                5
            )

        if not records:
            empty_label = ctk.CTkLabel(
                parent,
                text="No attendance records for today.",
                font=ctk.CTkFont(size=15),
                text_color="#777777"
            )

            empty_label.grid(
                row=1,
                column=0,
                columnspan=6,
                pady=40
            )

    except Exception as error:
        messagebox.showerror(
            "Database Error",
            str(error)
        )


def create_cell(parent, text, row, column):
    label = ctk.CTkLabel(
        parent,
        text=str(text) if text else "-",
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
