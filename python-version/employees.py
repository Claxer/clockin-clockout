import customtkinter as ctk
from tkinter import messagebox
import database


def show_employees(parent):
    employees_frame = ctk.CTkFrame(
        parent,
        fg_color="#f5f5f5",
        corner_radius=0
    )
    employees_frame.pack(fill="both", expand=True)

    # Header
    header_frame = ctk.CTkFrame(
        employees_frame,
        fg_color="transparent"
    )
    header_frame.pack(
        fill="x",
        padx=30,
        pady=(25, 15)
    )

    title = ctk.CTkLabel(
        header_frame,
        text="Employees",
        font=ctk.CTkFont(size=30, weight="bold"),
        text_color="#222222"
    )
    title.pack(side="left")

    add_button = ctk.CTkButton(
        header_frame,
        text="+ Add Employee",
        width=140,
        height=40,
        corner_radius=8,
        command=lambda: add_employee(parent)
    )
    add_button.pack(side="right")

    # Search bar
    search_frame = ctk.CTkFrame(
        employees_frame,
        fg_color="transparent"
    )
    search_frame.pack(
        fill="x",
        padx=30,
        pady=(0, 10)
    )

    search_entry = ctk.CTkEntry(
        search_frame,
        placeholder_text="Search employee...",
        height=40,
        width=300
    )
    search_entry.pack(side="left")

    search_button = ctk.CTkButton(
        search_frame,
        text="Search",
        width=90,
        height=40,
        command=lambda: load_employees(
            table_frame,
            search_entry.get()
        )
    )
    search_button.pack(
        side="left",
        padx=8
    )

    refresh_button = ctk.CTkButton(
        search_frame,
        text="Refresh",
        width=90,
        height=40,
        fg_color="#555555",
        hover_color="#444444",
        command=lambda: load_employees(
            table_frame
        )
    )
    refresh_button.pack(side="left")

    # Employee table
    table_container = ctk.CTkFrame(
        employees_frame,
        fg_color="white",
        corner_radius=12
    )
    table_container.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=(5, 25)
    )

    table_frame = ctk.CTkScrollableFrame(
        table_container,
        fg_color="white"
    )
    table_frame.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    load_employees(table_frame)


def load_employees(parent, search_text=""):
    # Clear existing records
    for widget in parent.winfo_children():
        widget.destroy()

    try:
        connection = database.get_connection()
        cursor = connection.cursor()

        if search_text.strip():
            cursor.execute(
                """
                SELECT id, name, position, department, contact
                FROM employees
                WHERE name LIKE ?
                OR position LIKE ?
                OR department LIKE ?
                """,
                (
                    "%" + search_text + "%",
                    "%" + search_text + "%",
                    "%" + search_text + "%"
                )
            )
        else:
            cursor.execute(
                """
                SELECT id, name, position, department, contact
                FROM employees
                ORDER BY id DESC
                """
            )

        employees = cursor.fetchall()

        connection.close()

        # Table headers
        headers = [
            "ID",
            "Name",
            "Position",
            "Department",
            "Contact",
            "Actions"
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

        # Make columns expand
        for column in range(6):
            parent.grid_columnconfigure(
                column,
                weight=1
            )

        # Employee records
        for row, employee in enumerate(employees, start=1):
            employee_id = employee[0]
            name = employee[1]
            position = employee[2]
            department = employee[3]
            contact = employee[4]

            create_cell(
                parent,
                employee_id,
                row,
                0
            )

            create_cell(
                parent,
                name,
                row,
                1
            )

            create_cell(
                parent,
                position,
                row,
                2
            )

            create_cell(
                parent,
                department,
                row,
                3
            )

            create_cell(
                parent,
                contact,
                row,
                4
            )

            # Action buttons
            action_frame = ctk.CTkFrame(
                parent,
                fg_color="transparent"
            )
            action_frame.grid(
                row=row,
                column=5,
                padx=5,
                pady=5
            )

            edit_button = ctk.CTkButton(
                action_frame,
                text="Edit",
                width=55,
                height=30,
                command=lambda emp=employee:
                edit_employee(emp, parent)
            )
            edit_button.pack(
                side="left",
                padx=2
            )

            delete_button = ctk.CTkButton(
                action_frame,
                text="Delete",
                width=60,
                height=30,
                fg_color="#555555",
                hover_color="#333333",
                command=lambda emp_id=employee_id:
                delete_employee(emp_id, parent)
            )
            delete_button.pack(
                side="left",
                padx=2
            )

        if not employees:
            empty_label = ctk.CTkLabel(
                parent,
                text="No employees found.",
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
            "Unable to load employees.\n\n" + str(error)
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


def add_employee(parent):
    window = ctk.CTkToplevel(parent)
    window.title("Add Employee")
    window.geometry("450x550")
    window.resizable(False, False)

    window.transient(parent)
    window.grab_set()

    title = ctk.CTkLabel(
        window,
        text="Add Employee",
        font=ctk.CTkFont(size=24, weight="bold")
    )
    title.pack(pady=(30, 25))

    name_entry = create_entry(
        window,
        "Full Name"
    )

    position_entry = create_entry(
        window,
        "Position"
    )

    department_entry = create_entry(
        window,
        "Department"
    )

    contact_entry = create_entry(
        window,
        "Contact Number"
    )

    def save_employee():
        name = name_entry.get().strip()
        position = position_entry.get().strip()
        department = department_entry.get().strip()
        contact = contact_entry.get().strip()

        if not name:
            messagebox.showwarning(
                "Missing Information",
                "Please enter the employee name."
            )
            return

        try:
            connection = database.get_connection()
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO employees
                (name, position, department, contact)
                VALUES (?, ?, ?, ?)
                """,
                (
                    name,
                    position,
                    department,
                    contact
                )
            )

            connection.commit()
            connection.close()

            messagebox.showinfo(
                "Success",
                "Employee added successfully."
            )

            window.destroy()

            show_employees(parent)

        except Exception as error:
            messagebox.showerror(
                "Database Error",
                str(error)
            )

    save_button = ctk.CTkButton(
        window,
        text="Save Employee",
        width=180,
        height=40,
        command=save_employee
    )
    save_button.pack(pady=25)


def edit_employee(employee, parent):
    window = ctk.CTkToplevel(parent)
    window.title("Edit Employee")
    window.geometry("450x550")
    window.resizable(False, False)

    window.transient(parent)
    window.grab_set()

    title = ctk.CTkLabel(
        window,
        text="Edit Employee",
        font=ctk.CTkFont(size=24, weight="bold")
    )
    title.pack(pady=(30, 25))

    name_entry = create_entry(
        window,
        "Full Name",
        employee[1]
    )

    position_entry = create_entry(
        window,
        "Position",
        employee[2]
    )

    department_entry = create_entry(
        window,
        "Department",
        employee[3]
    )

    contact_entry = create_entry(
        window,
        "Contact Number",
        employee[4]
    )

    def update_employee():
        name = name_entry.get().strip()
        position = position_entry.get().strip()
        department = department_entry.get().strip()
        contact = contact_entry.get().strip()

        if not name:
            messagebox.showwarning(
                "Missing Information",
                "Please enter the employee name."
            )
            return

        try:
            connection = database.get_connection()
            cursor = connection.cursor()

            cursor.execute(
                """
                UPDATE employees
                SET name = ?,
                    position = ?,
                    department = ?,
                    contact = ?
                WHERE id = ?
                """,
                (
                    name,
                    position,
                    department,
                    contact,
                    employee[0]
                )
            )

            connection.commit()
            connection.close()

            messagebox.showinfo(
                "Success",
                "Employee updated successfully."
            )

            window.destroy()

            show_employees(parent)

        except Exception as error:
            messagebox.showerror(
                "Database Error",
                str(error)
            )

    update_button = ctk.CTkButton(
        window,
        text="Save Changes",
        width=180,
        height=40,
        command=update_employee
    )
    update_button.pack(pady=25)


def delete_employee(employee_id, parent):
    answer = messagebox.askyesno(
        "Delete Employee",
        "Are you sure you want to delete this employee?"
    )

    if not answer:
        return

    try:
        connection = database.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM employees WHERE id = ?",
            (employee_id,)
        )

        connection.commit()
        connection.close()

        messagebox.showinfo(
            "Success",
            "Employee deleted successfully."
        )

        show_employees(parent)

    except Exception as error:
        messagebox.showerror(
            "Database Error",
            str(error)
        )


def create_entry(parent, placeholder, value=""):
    entry = ctk.CTkEntry(
        parent,
        placeholder_text=placeholder,
        width=330,
        height=40
    )

    entry.pack(
        padx=20,
        pady=7
    )

    if value:
        entry.insert(0, value)

    return entry
