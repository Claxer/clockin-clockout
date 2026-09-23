import customtkinter as ctk
from tkinter import messagebox

from database import (
    add_employee,
    update_employee,
    delete_employee,
    get_all_employees,
    get_active_attendance
)


class EmployeesPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.grid_rowconfigure(
            3,
            weight=1
        )

        self.selected_employee = None

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
            pady=(0, 20)
        )

        form = ctk.CTkFrame(
            self
        )

        form.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=(0, 15)
        )

        for i in range(4):
            form.grid_columnconfigure(
                i,
                weight=1
            )

        self.employee_id = ctk.CTkEntry(
            form,
            placeholder_text="Employee ID"
        )

        self.employee_id.grid(
            row=0,
            column=0,
            padx=8,
            pady=15,
            sticky="ew"
        )

        self.name = ctk.CTkEntry(
            form,
            placeholder_text="Employee Name"
        )

        self.name.grid(
            row=0,
            column=1,
            padx=8,
            pady=15,
            sticky="ew"
        )

        self.department = ctk.CTkEntry(
            form,
            placeholder_text="Department"
        )

        self.department.grid(
            row=0,
            column=2,
            padx=8,
            pady=15,
            sticky="ew"
        )

        self.position = ctk.CTkEntry(
            form,
            placeholder_text="Position"
        )

        self.position.grid(
            row=0,
            column=3,
            padx=8,
            pady=15,
            sticky="ew"
        )

        ctk.CTkButton(
            form,
            text="ADD EMPLOYEE",
            command=self.add
        ).grid(
            row=1,
            column=0,
            padx=8,
            pady=(0, 15),
            sticky="ew"
        )

        ctk.CTkButton(
            form,
            text="UPDATE",
            command=self.update
        ).grid(
            row=1,
            column=1,
            padx=8,
            pady=(0, 15),
            sticky="ew"
        )

        ctk.CTkButton(
            form,
            text="DELETE",
            fg_color="#c0392b",
            hover_color="#922b21",
            command=self.delete
        ).grid(
            row=1,
            column=2,
            padx=8,
            pady=(0, 15),
            sticky="ew"
        )

        ctk.CTkButton(
            form,
            text="CLEAR",
            command=self.clear_form
        ).grid(
            row=1,
            column=3,
            padx=8,
            pady=(0, 15),
            sticky="ew"
        )

        self.search = ctk.CTkEntry(
            self,
            placeholder_text="Search employee..."
        )

        self.search.grid(
            row=2,
            column=0,
            sticky="ew",
            pady=(0, 15)
        )

        self.search.bind(
            "<KeyRelease>",
            lambda event: self.load_employees()
        )

        self.employee_list = ctk.CTkScrollableFrame(
            self
        )

        self.employee_list.grid(
            row=3,
            column=0,
            sticky="nsew"
        )

    # =====================================================
    # ADD
    # =====================================================

    def add(self):
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

        if not department:
            messagebox.showwarning(
                "Missing Information",
                "Please enter a department."
            )

            return

        if not position:
            messagebox.showwarning(
                "Missing Information",
                "Please enter a position."
            )

            return

        success, message = add_employee(
            employee_id,
            name,
            department,
            position
        )

        if success:
            messagebox.showinfo(
                "Success",
                message
            )

            self.clear_form()
            self.load_employees()

        else:
            messagebox.showerror(
                "Error",
                message
            )

    # =====================================================
    # UPDATE
    # =====================================================

    def update(self):
        employee_id = self.employee_id.get().strip()
        name = self.name.get().strip()
        department = self.department.get().strip()
        position = self.position.get().strip()

        if not employee_id:
            messagebox.showwarning(
                "Missing ID",
                "Enter an employee ID."
            )

            return

        changed = update_employee(
            employee_id,
            name,
            department,
            position
        )

        if changed:
            messagebox.showinfo(
                "Updated",
                "Employee information updated."
            )

            self.clear_form()
            self.load_employees()

        else:
            messagebox.showerror(
                "Error",
                "Employee not found."
            )

    # =====================================================
    # DELETE
    # =====================================================

    def delete(self):
        employee_id = self.employee_id.get().strip()

        if not employee_id:
            messagebox.showwarning(
                "Missing ID",
                "Enter an employee ID."
            )

            return

        confirm = messagebox.askyesno(
            "Delete Employee",
            "Are you sure you want to delete this employee?"
        )

        if not confirm:
            return

        if get_active_attendance(employee_id):
            messagebox.showwarning(
                "Cannot Delete",
                "This employee is currently clocked in."
            )

            return

        deleted = delete_employee(
            employee_id
        )

        if deleted:
            messagebox.showinfo(
                "Deleted",
                "Employee deleted successfully."
            )

            self.clear_form()
            self.load_employees()

        else:
            messagebox.showerror(
                "Error",
                "Employee not found."
            )

    # =====================================================
    # LOAD EMPLOYEES
    # =====================================================

    def load_employees(self):
        for widget in self.employee_list.winfo_children():
            widget.destroy()

        search = self.search.get().strip()

        employees = get_all_employees(
            search
        )

        if not employees:
            ctk.CTkLabel(
                self.employee_list,
                text="No employees found.",
                text_color="gray"
            ).pack(
                pady=30
            )

            return

        headers = [
            "ID",
            "Name",
            "Department",
            "Position",
            "Status"
        ]

        header = ctk.CTkFrame(
            self.employee_list
        )

        header.pack(
            fill="x",
            pady=(0, 5)
        )

        for text in headers:
            ctk.CTkLabel(
                header,
                text=text,
                font=("Arial", 12, "bold")
            ).pack(
                side="left",
                expand=True,
                fill="x",
                pady=10
            )

        for employee in employees:
            row = ctk.CTkFrame(
                self.employee_list
            )

            row.pack(
                fill="x",
                pady=2
            )

            if get_active_attendance(
                employee["employee_id"]
            ):
                status = "Working"
            else:
                status = "Off Duty"

            values = [
                employee["employee_id"],
                employee["name"],
                employee["department"],
                employee["position"],
                status
            ]

            for value in values:
                ctk.CTkLabel(
                    row,
                    text=value
                ).pack(
                    side="left",
                    expand=True,
                    fill="x",
                    pady=8
                )

            row.bind(
                "<Button-1>",
                lambda event, e=employee:
                self.select_employee(e)
            )

            for child in row.winfo_children():
                child.bind(
                    "<Button-1>",
                    lambda event, e=employee:
                    self.select_employee(e)
                )

    # =====================================================
    # SELECT
    # =====================================================

    def select_employee(self, employee):
        self.clear_form()

        self.employee_id.insert(
            0,
            employee["employee_id"]
        )

        self.name.insert(
            0,
            employee["name"]
        )

        self.department.insert(
            0,
            employee["department"]
        )

        self.position.insert(
            0,
            employee["position"]
        )

    # =====================================================
    # CLEAR
    # =====================================================

    def clear_form(self):
        self.employee_id.delete(
            0,
            "end"
        )

        self.name.delete(
            0,
            "end"
        )

        self.department.delete(
            0,
            "end"
        )

        self.position.delete(
            0,
            "end"
        )
