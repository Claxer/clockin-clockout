import customtkinter as ctk
from tkinter import messagebox

from database import connect_db


class EmployeesPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.create_ui()

        self.load_employees()

    # =====================================================
    # UI
    # =====================================================

    def create_ui(self):

        title = ctk.CTkLabel(
            self,
            text="Employee Management",
            font=("Arial", 30, "bold")
        )

        title.grid(
            row=0,
            column=0,
            sticky="w",
            pady=(10, 20)
        )

        # Input area
        input_frame = ctk.CTkFrame(self)

        input_frame.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=5
        )

        self.employee_id = ctk.CTkEntry(
            input_frame,
            placeholder_text="Employee ID"
        )

        self.employee_id.grid(
            row=0,
            column=0,
            padx=10,
            pady=15
        )

        self.name = ctk.CTkEntry(
            input_frame,
            placeholder_text="Employee Name"
        )

        self.name.grid(
            row=0,
            column=1,
            padx=10,
            pady=15
        )

        self.department = ctk.CTkEntry(
            input_frame,
            placeholder_text="Department"
        )

        self.department.grid(
            row=0,
            column=2,
            padx=10,
            pady=15
        )

        self.position = ctk.CTkEntry(
            input_frame,
            placeholder_text="Position"
        )

        self.position.grid(
            row=0,
            column=3,
            padx=10,
            pady=15
        )

        ctk.CTkButton(
            input_frame,
            text="ADD EMPLOYEE",
            command=self.add_employee
        ).grid(
            row=0,
            column=4,
            padx=10
        )

        # Search
        self.search = ctk.CTkEntry(
            self,
            placeholder_text="Search employee..."
        )

        self.search.grid(
            row=2,
            column=0,
            sticky="ew",
            pady=10
        )

        self.search.bind(
            "<KeyRelease>",
            lambda event: self.load_employees()
        )

        # Employee list
        self.employee_list = ctk.CTkScrollableFrame(
            self
        )

        self.employee_list.grid(
            row=3,
            column=0,
            sticky="nsew"
        )

    # =====================================================
    # ADD EMPLOYEE
    # =====================================================

    def add_employee(self):

        employee_id = self.employee_id.get().strip()
        name = self.name.get().strip()
        department = self.department.get().strip()
        position = self.position.get().strip()

        if not employee_id or not name:
            messagebox.showwarning(
                "Missing Information",
                "Employee ID and name are required."
            )
            return

        conn = connect_db()
        cursor = conn.cursor()

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

            conn.commit()

            messagebox.showinfo(
                "Success",
                f"{name} has been added."
            )

            self.clear_inputs()
            self.load_employees()

        except Exception:

            messagebox.showerror(
                "Error",
                "Employee ID already exists."
            )

        conn.close()

    # =====================================================
    # LOAD EMPLOYEES
    # =====================================================

    def load_employees(self):

        for widget in self.employee_list.winfo_children():
            widget.destroy()

        search = self.search.get().strip()

        conn = connect_db()
        cursor = conn.cursor()

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
            ORDER BY name
        """, (
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        ))

        employees = cursor.fetchall()

        conn.close()

        for employee in employees:

            employee_id = employee[0]
            name = employee[1]
            department = employee[2]
            position = employee[3]

            row = ctk.CTkFrame(
                self.employee_list
            )

            row.pack(
                fill="x",
                pady=5
            )

            info = (
                f"{employee_id}   |   "
                f"{name}   |   "
                f"{department}   |   "
                f"{position}"
            )

            ctk.CTkLabel(
                row,
                text=info,
                font=("Arial", 13),
                anchor="w"
            ).pack(
                side="left",
                padx=15,
                pady=12
            )

            ctk.CTkButton(
                row,
                text="DELETE",
                width=80,
                fg_color="#8B0000",
                hover_color="#A00000",
                command=lambda id=employee_id:
                    self.delete_employee(id)
            ).pack(
                side="right",
                padx=10
            )

    # =====================================================
    # DELETE
    # =====================================================

    def delete_employee(self, employee_id):

        confirm = messagebox.askyesno(
            "Delete Employee",
            f"Delete employee {employee_id}?"
        )

        if not confirm:
            return

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM employees
            WHERE employee_id = ?
        """, (employee_id,))

        cursor.execute("""
            DELETE FROM attendance
            WHERE employee_id = ?
        """, (employee_id,))

        conn.commit()
        conn.close()

        self.load_employees()

    # =====================================================
    # CLEAR
    # =====================================================

    def clear_inputs(self):

        self.employee_id.delete(0, "end")
        self.name.delete(0, "end")
        self.department.delete(0, "end")
        self.position.delete(0, "end")
