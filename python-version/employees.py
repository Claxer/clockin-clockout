import customtkinter as ctk
from tkinter import ttk, messagebox

import database


class EmployeesPage:

    def __init__(self, parent):

        self.parent = parent

        # ----------------------------------------------------
        # COLORS
        # ----------------------------------------------------

        self.background = "#F5F5F7"
        self.card_color = "#FFFFFF"
        self.text_color = "#1D1D1F"
        self.secondary_text = "#6E6E73"
        self.blue = "#0071E3"
        self.red = "#FF3B30"
        self.border = "#E5E5E7"

        # ----------------------------------------------------
        # MAIN FRAME
        # ----------------------------------------------------

        self.frame = ctk.CTkFrame(
            self.parent,
            fg_color=self.background,
            corner_radius=0
        )

        self.frame.pack(
            fill="both",
            expand=True
        )

        self.create_page()

    # ========================================================
    # PAGE
    # ========================================================

    def create_page(self):

        # ----------------------------------------------------
        # TITLE
        # ----------------------------------------------------

        header = ctk.CTkFrame(
            self.frame,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            padx=30,
            pady=(25, 10)
        )

        title = ctk.CTkLabel(
            header,
            text="Employees",
            font=ctk.CTkFont(
                size=28,
                weight="bold"
            ),
            text_color=self.text_color
        )

        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            header,
            text="Add, search, and manage company employees",
            font=ctk.CTkFont(size=13),
            text_color=self.secondary_text
        )

        subtitle.pack(anchor="w")

        # ----------------------------------------------------
        # ADD EMPLOYEE CARD
        # ----------------------------------------------------

        self.create_employee_form()

        # ----------------------------------------------------
        # EMPLOYEE LIST
        # ----------------------------------------------------

        self.create_employee_list()

    # ========================================================
    # EMPLOYEE FORM
    # ========================================================

    def create_employee_form(self):

        self.form_card = ctk.CTkFrame(
            self.frame,
            fg_color=self.card_color,
            corner_radius=15,
            border_width=1,
            border_color=self.border
        )

        self.form_card.pack(
            fill="x",
            padx=30,
            pady=(5, 15)
        )

        title = ctk.CTkLabel(
            self.form_card,
            text="Add New Employee",
            font=ctk.CTkFont(
                size=17,
                weight="bold"
            ),
            text_color=self.text_color
        )

        title.pack(
            anchor="w",
            padx=25,
            pady=(20, 15)
        )

        fields = ctk.CTkFrame(
            self.form_card,
            fg_color="transparent"
        )

        fields.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        # Employee ID
        self.employee_id_entry = self.create_field(
            fields,
            "Employee ID",
            "EMP-001"
        )

        # Name
        self.name_entry = self.create_field(
            fields,
            "Full Name",
            "Juan Dela Cruz"
        )

        # Department
        self.department_entry = self.create_field(
            fields,
            "Department",
            "Information Technology"
        )

        # Position
        self.position_entry = self.create_field(
            fields,
            "Position",
            "Staff"
        )

        # Add button
        add_button = ctk.CTkButton(
            fields,
            text="Add Employee",
            width=135,
            height=40,
            corner_radius=8,
            fg_color=self.blue,
            hover_color="#0062C4",
            font=ctk.CTkFont(
                size=13,
                weight="bold"
            ),
            command=self.add_employee
        )

        add_button.pack(
            side="left",
            padx=7,
            pady=(22, 0)
        )

    # ========================================================
    # CREATE FORM FIELD
    # ========================================================

    def create_field(
        self,
        parent,
        label_text,
        placeholder
    ):

        container = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )

        container.pack(
            side="left",
            fill="x",
            expand=True,
            padx=5
        )

        label = ctk.CTkLabel(
            container,
            text=label_text,
            font=ctk.CTkFont(
                size=11,
                weight="bold"
            ),
            text_color=self.secondary_text
        )

        label.pack(
            anchor="w"
        )

        entry = ctk.CTkEntry(
            container,
            height=40,
            corner_radius=8,
            placeholder_text=placeholder
        )

        entry.pack(
            fill="x",
            pady=(5, 0)
        )

        return entry

    # ========================================================
    # EMPLOYEE LIST
    # ========================================================

    def create_employee_list(self):

        title_frame = ctk.CTkFrame(
            self.frame,
            fg_color="transparent"
        )

        title_frame.pack(
            fill="x",
            padx=30,
            pady=(5, 5)
        )

        title = ctk.CTkLabel(
            title_frame,
            text="Employee List",
            font=ctk.CTkFont(
                size=18,
                weight="bold"
            ),
            text_color=self.text_color
        )

        title.pack(side="left")

        # ----------------------------------------------------
        # SEARCH
        # ----------------------------------------------------

        self.search_entry = ctk.CTkEntry(
            title_frame,
            width=250,
            height=38,
            corner_radius=8,
            placeholder_text="Search employees..."
        )

        self.search_entry.pack(
            side="right",
            padx=(10, 0)
        )

        search_button = ctk.CTkButton(
            title_frame,
            text="Search",
            width=85,
            height=38,
            corner_radius=8,
            command=self.search_employees
        )

        search_button.pack(
            side="right"
        )

        show_all_button = ctk.CTkButton(
            title_frame,
            text="Show All",
            width=85,
            height=38,
            corner_radius=8,
            fg_color="#E5E5E7",
            hover_color="#D5D5D7",
            text_color=self.text_color,
            command=self.load_employees
        )

        show_all_button.pack(
            side="right",
            padx=5
        )

        # ----------------------------------------------------
        # TABLE CARD
        # ----------------------------------------------------

        self.table_card = ctk.CTkFrame(
            self.frame,
            fg_color=self.card_color,
            corner_radius=15,
            border_width=1,
            border_color=self.border
        )

        self.table_card.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(5, 10)
        )

        # ----------------------------------------------------
        # TABLE
        # ----------------------------------------------------

        self.setup_table()

        # ----------------------------------------------------
        # DELETE BUTTON
        # ----------------------------------------------------

        delete_button = ctk.CTkButton(
            self.frame,
            text="Delete Selected Employee",
            width=210,
            height=40,
            corner_radius=8,
            fg_color=self.red,
            hover_color="#D93025",
            font=ctk.CTkFont(
                size=13,
                weight="bold"
            ),
            command=self.delete_employee
        )

        delete_button.pack(
            anchor="e",
            padx=30,
            pady=(0, 20)
        )

    # ========================================================
    # TABLE
    # ========================================================

    def setup_table(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "Treeview",
            rowheight=40,
            font=("Segoe UI", 10),
            background="#FFFFFF",
            fieldbackground="#FFFFFF",
            borderwidth=0
        )

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold"),
            background="#F0F0F2",
            foreground="#1D1D1F",
            padding=8
        )

        style.map(
            "Treeview",
            background=[
                ("selected", "#DCEBFA")
            ],
            foreground=[
                ("selected", "#1D1D1F")
            ]
        )

        self.employee_table = ttk.Treeview(
            self.table_card,
            columns=(
                "employee_id",
                "name",
                "department",
                "position"
            ),
            show="headings"
        )

        self.employee_table.heading(
            "employee_id",
            text="Employee ID"
        )

        self.employee_table.heading(
            "name",
            text="Full Name"
        )

        self.employee_table.heading(
            "department",
            text="Department"
        )

        self.employee_table.heading(
            "position",
            text="Position"
        )

        self.employee_table.column(
            "employee_id",
            width=130,
            anchor="center"
        )

        self.employee_table.column(
            "name",
            width=230
        )

        self.employee_table.column(
            "department",
            width=250
        )

        self.employee_table.column(
            "position",
            width=180
        )

        self.employee_table.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.load_employees()

    # ========================================================
    # LOAD EMPLOYEES
    # ========================================================

    def load_employees(self):

        for item in self.employee_table.get_children():

            self.employee_table.delete(item)

        employees = database.get_all_employees()

        self.insert_employees(
            employees
        )

    # ========================================================
    # INSERT EMPLOYEES INTO TABLE
    # ========================================================

    def insert_employees(self, employees):

        for employee in employees:

            self.employee_table.insert(
                "",
                "end",
                values=(
                    employee[0],
                    employee[1],
                    employee[2],
                    employee[3]
                )
            )

    # ========================================================
    # SEARCH EMPLOYEES
    # ========================================================

    def search_employees(self):

        search_text = (
            self.search_entry
            .get()
            .strip()
        )

        if not search_text:

            self.load_employees()

            return

        for item in self.employee_table.get_children():

            self.employee_table.delete(item)

        employees = database.search_employees(
            search_text
        )

        self.insert_employees(
            employees
        )

    # ========================================================
    # ADD EMPLOYEE
    # ========================================================

    def add_employee(self):

        employee_id = (
            self.employee_id_entry
            .get()
            .strip()
        )

        name = (
            self.name_entry
            .get()
            .strip()
        )

        department = (
            self.department_entry
            .get()
            .strip()
        )

        position = (
            self.position_entry
            .get()
            .strip()
        )

        # ----------------------------------------------------
        # VALIDATION
        # ----------------------------------------------------

        if not employee_id:

            messagebox.showwarning(
                "Missing Employee ID",
                "Please enter an employee ID."
            )

            return

        if not name:

            messagebox.showwarning(
                "Missing Name",
                "Please enter the employee's name."
            )

            return

        if not department:

            messagebox.showwarning(
                "Missing Department",
                "Please enter the employee's department."
            )

            return

        if not position:

            messagebox.showwarning(
                "Missing Position",
                "Please enter the employee's position."
            )

            return

        # ----------------------------------------------------
        # SAVE EMPLOYEE
        # ----------------------------------------------------

        success = database.add_employee(
            employee_id,
            name,
            department,
            position
        )

        if not success:

            messagebox.showerror(
                "Employee Already Exists",
                "That employee ID is already registered."
            )

            return

        messagebox.showinfo(
            "Employee Added",
            f"{name} has been added successfully."
        )

        self.clear_form()

        self.load_employees()

    # ========================================================
    # CLEAR FORM
    # ========================================================

    def clear_form(self):

        self.employee_id_entry.delete(
            0,
            "end"
        )

        self.name_entry.delete(
            0,
            "end"
        )

        self.department_entry.delete(
            0,
            "end"
        )

        self.position_entry.delete(
            0,
            "end"
        )

    # ========================================================
    # DELETE EMPLOYEE
    # ========================================================

    def delete_employee(self):

        selected = (
            self.employee_table
            .selection()
        )

        if not selected:

            messagebox.showwarning(
                "No Employee Selected",
                "Please select an employee from the table."
            )

            return

        values = self.employee_table.item(
            selected[0],
            "values"
        )

        employee_id = values[0]
        employee_name = values[1]

        confirmation = messagebox.askyesno(
            "Delete Employee",
            f"Are you sure you want to delete\n\n"
            f"{employee_name} ({employee_id})?"
        )

        if not confirmation:

            return

        database.delete_employee(
            employee_id
        )

        messagebox.showinfo(
            "Employee Deleted",
            f"{employee_name} has been removed."
        )

        self.load_employees()

    # ========================================================
    # REFRESH
    # ========================================================

    def refresh(self):

        self.load_employees()
