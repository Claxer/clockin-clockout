import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
import database


def show_reports(parent):
    reports_frame = ctk.CTkFrame(
        parent,
        fg_color="#f5f5f5",
        corner_radius=0
    )
    reports_frame.pack(
        fill="both",
        expand=True
    )

    # Header
    header_frame = ctk.CTkFrame(
        reports_frame,
        fg_color="transparent"
    )
    header_frame.pack(
        fill="x",
        padx=30,
        pady=(25, 15)
    )

    title = ctk.CTkLabel(
        header_frame,
        text="Attendance Reports",
        font=ctk.CTkFont(
            size=30,
            weight="bold"
        ),
        text_color="#222222"
    )
    title.pack(side="left")

    # Filter section
    filter_frame = ctk.CTkFrame(
        reports_frame,
        fg_color="white",
        corner_radius=12
    )
    filter_frame.pack(
        fill="x",
        padx=30,
        pady=(0, 15)
    )

    filter_title = ctk.CTkLabel(
        filter_frame,
        text="Report Filters",
        font=ctk.CTkFont(
            size=18,
            weight="bold"
        ),
        text_color="#222222"
    )
    filter_title.pack(
        anchor="w",
        padx=20,
        pady=(15, 10)
    )

    controls_frame = ctk.CTkFrame(
        filter_frame,
        fg_color="transparent"
    )
    controls_frame.pack(
        fill="x",
        padx=20,
        pady=(0, 20)
    )

    # Start date
    start_label = ctk.CTkLabel(
        controls_frame,
        text="Start Date",
        font=ctk.CTkFont(size=13),
        text_color="#555555"
    )
    start_label.grid(
        row=0,
        column=0,
        padx=(0, 8),
        sticky="w"
    )

    start_entry = ctk.CTkEntry(
        controls_frame,
        width=130,
        height=38,
        placeholder_text="YYYY-MM-DD"
    )
    start_entry.grid(
        row=1,
        column=0,
        padx=(0, 15),
        pady=(5, 0)
    )

    # End date
    end_label = ctk.CTkLabel(
        controls_frame,
        text="End Date",
        font=ctk.CTkFont(size=13),
        text_color="#555555"
    )
    end_label.grid(
        row=0,
        column=1,
        padx=(0, 8),
        sticky="w"
    )

    end_entry = ctk.CTkEntry(
        controls_frame,
        width=130,
        height=38,
        placeholder_text="YYYY-MM-DD"
    )
    end_entry.grid(
        row=1,
        column=1,
        padx=(0, 15),
        pady=(5, 0)
    )

    # Employee filter
    employee_label = ctk.CTkLabel(
        controls_frame,
        text="Employee",
        font=ctk.CTkFont(size=13),
        text_color="#555555"
    )
    employee_label.grid(
        row=0,
        column=2,
        padx=(0, 8),
        sticky="w"
    )

    employees = get_employees()

    employee_values = ["All Employees"]

    for employee in employees:
        employee_values.append(
            f"{employee[0]} - {employee[1]}"
        )

    employee_dropdown = ctk.CTkComboBox(
        controls_frame,
        values=employee_values,
        width=200,
        height=38
    )
    employee_dropdown.set("All Employees")
    employee_dropdown.grid(
        row=1,
        column=2,
        padx=(0, 15),
        pady=(5, 0)
    )

    # Generate button
    generate_button = ctk.CTkButton(
        controls_frame,
        text="Generate Report",
        width=140,
        height=38,
        command=lambda: generate_report(
            report_table,
            summary_frame,
            start_entry.get(),
            end_entry.get(),
            employee_dropdown.get()
        )
    )
    generate_button.grid(
        row=1,
        column=3,
        padx=5,
        pady=(5, 0)
    )

    # Today button
    today_button = ctk.CTkButton(
        controls_frame,
        text="Today",
        width=80,
        height=38,
        fg_color="#555555",
        hover_color="#444444",
        command=lambda: load_today(
            start_entry,
            end_entry,
            report_table,
            summary_frame,
            employee_dropdown
        )
    )
    today_button.grid(
        row=1,
        column=4,
        padx=5,
        pady=(5, 0)
    )

    # Summary
    summary_frame = ctk.CTkFrame(
        reports_frame,
        fg_color="transparent"
    )
    summary_frame.pack(
        fill="x",
        padx=30,
        pady=(0, 15)
    )

    # Report table
    table_container = ctk.CTkFrame(
        reports_frame,
        fg_color="white",
        corner_radius=12
    )
    table_container.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=(0, 25)
    )

    report_table = ctk.CTkScrollableFrame(
        table_container,
        fg_color="white"
    )
    report_table.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    # Automatically show today's records
    load_today(
        start_entry,
        end_entry,
        report_table,
        summary_frame,
        employee_dropdown
    )


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


def load_today(
    start_entry,
    end_entry,
    report_table,
    summary_frame,
    employee_dropdown
):
    today = datetime.now().strftime("%Y-%m-%d")

    start_entry.delete(0, "end")
    start_entry.insert(0, today)

    end_entry.delete(0, "end")
    end_entry.insert(0, today)

    employee_dropdown.set("All Employees")

    generate_report(
        report_table,
        summary_frame,
        today,
        today,
        "All Employees"
    )


def generate_report(
    report_table,
    summary_frame,
    start_date,
    end_date,
    selected_employee
):
    # Validate dates
    try:
        start = datetime.strptime(
            start_date,
            "%Y-%m-%d"
        )

        end = datetime.strptime(
            end_date,
            "%Y-%m-%d"
        )

    except ValueError:
        messagebox.showwarning(
            "Invalid Date",
            "Please enter dates using YYYY-MM-DD."
        )
        return

    if start > end:
        messagebox.showwarning(
            "Invalid Date Range",
            "Start date cannot be after the end date."
        )
        return

    # Clear old table
    for widget in report_table.winfo_children():
        widget.destroy()

    # Clear old summary
    for widget in summary_frame.winfo_children():
        widget.destroy()

    try:
        connection = database.get_connection()
        cursor = connection.cursor()

        query = """
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
            WHERE attendance.date BETWEEN ? AND ?
        """

        parameters = [
            start_date,
            end_date
        ]

        # Employee filter
        if selected_employee != "All Employees":
            try:
                employee_id = int(
                    selected_employee.split(" - ")[0]
                )

                query += " AND attendance.employee_id = ?"

                parameters.append(employee_id)

            except ValueError:
                pass

        query += """
            ORDER BY attendance.date DESC,
                     attendance.id DESC
        """

        cursor.execute(
            query,
            parameters
        )

        records = cursor.fetchall()

        connection.close()

        # Calculate summary
        total_records = len(records)

        present_count = 0
        late_count = 0
        completed_count = 0

        for record in records:
            status = record[5]

            if status == "Present":
                present_count += 1

            elif status == "Late":
                late_count += 1

            if record[4]:
                completed_count += 1

        # Summary cards
        create_summary_card(
            summary_frame,
            "Total Records",
            total_records,
            0
        )

        create_summary_card(
            summary_frame,
            "Present",
            present_count,
            1
        )

        create_summary_card(
            summary_frame,
            "Late",
            late_count,
            2
        )

        create_summary_card(
            summary_frame,
            "Completed",
            completed_count,
            3
        )

        # Table headers
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
                report_table,
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

            report_table.grid_columnconfigure(
                column,
                weight=1
            )

        # Records
        for row, record in enumerate(
            records,
            start=1
        ):
            create_cell(
                report_table,
                record[0],
                row,
                0
            )

            create_cell(
                report_table,
                record[1],
                row,
                1
            )

            create_cell(
                report_table,
                record[2],
                row,
                2
            )

            create_cell(
                report_table,
                record[3] or "-",
                row,
                3
            )

            create_cell(
                report_table,
                record[4] or "-",
                row,
                4
            )

            create_cell(
                report_table,
                record[5],
                row,
                5
            )

        if not records:
            empty_label = ctk.CTkLabel(
                report_table,
                text="No attendance records found.",
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


def create_summary_card(
    parent,
    title,
    value,
    column
):
    card = ctk.CTkFrame(
        parent,
        fg_color="white",
        corner_radius=10,
        height=80
    )

    card.grid(
        row=0,
        column=column,
        padx=5,
        sticky="nsew"
    )

    parent.grid_columnconfigure(
        column,
        weight=1
    )

    title_label = ctk.CTkLabel(
        card,
        text=title,
        font=ctk.CTkFont(size=12),
        text_color="#777777"
    )

    title_label.pack(
        anchor="w",
        padx=15,
        pady=(12, 0)
    )

    value_label = ctk.CTkLabel(
        card,
        text=str(value),
        font=ctk.CTkFont(
            size=22,
            weight="bold"
        ),
        text_color="#222222"
    )

    value_label.pack(
        anchor="w",
        padx=15
    )


def create_cell(
    parent,
    text,
    row,
    column
):
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
