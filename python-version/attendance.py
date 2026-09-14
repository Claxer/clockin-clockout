import customtkinter as ctk
from tkinter import ttk, messagebox
from datetime import datetime

import database


class AttendancePage:

    def __init__(self, parent):

        self.parent = parent

        # ====================================================
        # COLORS
        # ====================================================

        self.background = "#F5F5F7"
        self.card_color = "#FFFFFF"
        self.text_color = "#1D1D1F"
        self.secondary_text = "#6E6E73"

        self.blue = "#0071E3"
        self.green = "#34C759"
        self.red = "#FF3B30"
        self.orange = "#FF9500"

        self.border = "#E5E5E7"

        # ====================================================
        # MAIN FRAME
        # ====================================================

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
    # CREATE PAGE
    # ========================================================

    def create_page(self):

        # ----------------------------------------------------
        # HEADER
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
            text="Attendance",
            font=ctk.CTkFont(
                size=28,
                weight="bold"
            ),
            text_color=self.text_color
        )

        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            header,
            text="Clock employees in and out and monitor working hours",
            font=ctk.CTkFont(
                size=13
            ),
            text_color=self.secondary_text
        )

        subtitle.pack(anchor="w")

        # ----------------------------------------------------
        # QUICK ATTENDANCE
        # ----------------------------------------------------

        self.create_quick_attendance()

        # ----------------------------------------------------
        # ATTENDANCE HISTORY
        # ----------------------------------------------------

        self.create_attendance_history()

    # ========================================================
    # QUICK ATTENDANCE
    # ========================================================

    def create_quick_attendance(self):

        card = ctk.CTkFrame(
            self.frame,
            fg_color=self.card_color,
            corner_radius=15,
            border_width=1,
            border_color=self.border
        )

        card.pack(
            fill="x",
            padx=30,
            pady=(5, 15)
        )

        # ----------------------------------------------------
        # CARD TITLE
        # ----------------------------------------------------

        title = ctk.CTkLabel(
            card,
            text="Quick Attendance",
            font=ctk.CTkFont(
                size=18,
                weight="bold"
            ),
            text_color=self.text_color
        )

        title.pack(
            anchor="w",
            padx=25,
            pady=(20, 5)
        )

        description = ctk.CTkLabel(
            card,
            text="Enter an employee ID to record their attendance.",
            font=ctk.CTkFont(
                size=12
            ),
            text_color=self.secondary_text
        )

        description.pack(
            anchor="w",
            padx=25
        )

        # ----------------------------------------------------
        # INPUT AREA
        # ----------------------------------------------------

        input_frame = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        input_frame.pack(
            fill="x",
            padx=25,
            pady=20
        )

        self.employee_id_entry = ctk.CTkEntry(
            input_frame,
            height=42,
            corner_radius=8,
            placeholder_text="Employee ID  •  EMP-001"
        )

        self.employee_id_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        # ----------------------------------------------------
        # CLOCK IN BUTTON
        # ----------------------------------------------------

        clock_in_button = ctk.CTkButton(
            input_frame,
            text="Clock In",
            width=125,
            height=42,
            corner_radius=8,
            fg_color=self.green,
            hover_color="#28A745",
            font=ctk.CTkFont(
                size=13,
                weight="bold"
            ),
            command=self.clock_in
        )

        clock_in_button.pack(
            side="left",
            padx=5
        )

        # ----------------------------------------------------
        # CLOCK OUT BUTTON
        # ----------------------------------------------------

        clock_out_button = ctk.CTkButton(
            input_frame,
            text="Clock Out",
            width=125,
            height=42,
            corner_radius=8,
            fg_color=self.red,
            hover_color="#D93025",
            font=ctk.CTkFont(
                size=13,
                weight="bold"
            ),
            command=self.clock_out
        )

        clock_out_button.pack(
            side="left",
            padx=5
        )

        # ----------------------------------------------------
        # CLEAR BUTTON
        # ----------------------------------------------------

        clear_button = ctk.CTkButton(
            input_frame,
            text="Clear",
            width=80,
            height=42,
            corner_radius=8,
            fg_color="#E5E5E7",
            hover_color="#D5D5D7",
            text_color=self.text_color,
            command=self.clear_employee_id
        )

        clear_button.pack(
            side="left",
            padx=5
        )

    # ========================================================
    # ATTENDANCE HISTORY
    # ========================================================

    def create_attendance_history(self):

        # ----------------------------------------------------
        # TITLE + SEARCH
        # ----------------------------------------------------

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
            text="Attendance Records",
            font=ctk.CTkFont(
                size=18,
                weight="bold"
            ),
            text_color=self.text_color
        )

        title.pack(
            side="left"
        )

        # ----------------------------------------------------
        # SEARCH
        # ----------------------------------------------------

        self.search_entry = ctk.CTkEntry(
            title_frame,
            width=250,
            height=38,
            corner_radius=8,
            placeholder_text="Search ID or employee name..."
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
            command=self.search_attendance
        )

        search_button.pack(
            side="right"
        )

        # ----------------------------------------------------
        # TODAY BUTTON
        # ----------------------------------------------------

        today_button = ctk.CTkButton(
            title_frame,
            text="Today",
            width=85,
            height=38,
            corner_radius=8,
            fg_color="#E5E5E7",
            hover_color="#D5D5D7",
            text_color=self.text_color,
            command=self.load_today
        )

        today_button.pack(
            side="right",
            padx=5
        )

        # ----------------------------------------------------
        # SHOW ALL BUTTON
        # ----------------------------------------------------

        all_button = ctk.CTkButton(
            title_frame,
            text="Show All",
            width=85,
            height=38,
            corner_radius=8,
            fg_color="#E5E5E7",
            hover_color="#D5D5D7",
            text_color=self.text_color,
            command=self.load_all
        )

        all_button.pack(
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
            pady=(5, 20)
        )

        self.setup_table()

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

        self.attendance_table = ttk.Treeview(
            self.table_card,
            columns=(
                "employee_id",
                "name",
                "clock_in",
                "clock_out",
                "hours",
                "status"
            ),
            show="headings"
        )

        # ----------------------------------------------------
        # HEADINGS
        # ----------------------------------------------------

        self.attendance_table.heading(
            "employee_id",
            text="Employee ID"
        )

        self.attendance_table.heading(
            "name",
            text="Employee Name"
        )

        self.attendance_table.heading(
            "clock_in",
            text="Clock In"
        )

        self.attendance_table.heading(
            "clock_out",
            text="Clock Out"
        )

        self.attendance_table.heading(
            "hours",
            text="Working Hours"
        )

        self.attendance_table.heading(
            "status",
            text="Status"
        )

        # ----------------------------------------------------
        # COLUMN WIDTHS
        # ----------------------------------------------------

        self.attendance_table.column(
            "employee_id",
            width=120,
            anchor="center"
        )

        self.attendance_table.column(
            "name",
            width=200
        )

        self.attendance_table.column(
            "clock_in",
            width=170
        )

        self.attendance_table.column(
            "clock_out",
            width=170
        )

        self.attendance_table.column(
            "hours",
            width=120,
            anchor="center"
        )

        self.attendance_table.column(
            "status",
            width=120,
            anchor="center"
        )

        # ----------------------------------------------------
        # TABLE
        # ----------------------------------------------------

        self.attendance_table.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # ----------------------------------------------------
        # LOAD TODAY'S RECORDS
        # ----------------------------------------------------

        self.load_today()

    # ========================================================
    # CLOCK IN
    # ========================================================

    def clock_in(self):

        employee_id = (
            self.employee_id_entry
            .get()
            .strip()
        )

        if not employee_id:

            messagebox.showwarning(
                "Missing Employee ID",
                "Please enter an employee ID."
            )

            return

        # ----------------------------------------------------
        # FIND EMPLOYEE
        # ----------------------------------------------------

        employee = database.get_employee(
            employee_id
        )

        if not employee:

            messagebox.showerror(
                "Employee Not Found",
                "This employee ID is not registered."
            )

            return

        # ----------------------------------------------------
        # CHECK CURRENT STATUS
        # ----------------------------------------------------

        active_record = (
            database.get_active_attendance(
                employee_id
            )
        )

        if active_record:

            messagebox.showwarning(
                "Already Clocked In",
                f"{employee[1]} is already clocked in."
            )

            return

        # ----------------------------------------------------
        # CURRENT TIME
        # ----------------------------------------------------

        current_time = datetime.now()

        clock_in_time = current_time.strftime(
            "%Y-%m-%d %I:%M:%S %p"
        )

        # ----------------------------------------------------
        # SAVE ATTENDANCE
        # ----------------------------------------------------

        database.add_attendance(
            employee_id,
            employee[1],
            clock_in_time
        )

        messagebox.showinfo(
            "Clock In Successful",
            f"{employee[1]} has successfully clocked in.\n\n"
            f"Time: {current_time.strftime('%I:%M:%S %p')}"
        )

        self.clear_employee_id()

        self.load_today()

    # ========================================================
    # CLOCK OUT
    # ========================================================

    def clock_out(self):

        employee_id = (
            self.employee_id_entry
            .get()
            .strip()
        )

        if not employee_id:

            messagebox.showwarning(
                "Missing Employee ID",
                "Please enter an employee ID."
            )

            return

        # ----------------------------------------------------
        # FIND ACTIVE ATTENDANCE
        # ----------------------------------------------------

        active_record = (
            database.get_active_attendance(
                employee_id
            )
        )

        if not active_record:

            messagebox.showwarning(
                "Not Clocked In",
                "This employee does not have an active clock-in record."
            )

            return

        attendance_id = active_record[0]
        employee_name = active_record[2]
        clock_in_string = active_record[3]

        # ----------------------------------------------------
        # CONVERT CLOCK-IN TIME
        # ----------------------------------------------------

        try:

            clock_in_time = datetime.strptime(
                clock_in_string,
                "%Y-%m-%d %I:%M:%S %p"
            )

        except ValueError:

            messagebox.showerror(
                "Time Error",
                "The clock-in time could not be read."
            )

            return

        # ----------------------------------------------------
        # CURRENT TIME
        # ----------------------------------------------------

        clock_out_time = datetime.now()

        clock_out_string = (
            clock_out_time.strftime(
                "%Y-%m-%d %I:%M:%S %p"
            )
        )

        # ----------------------------------------------------
        # CALCULATE WORKING TIME
        # ----------------------------------------------------

        difference = (
            clock_out_time - clock_in_time
        )

        total_seconds = int(
            difference.total_seconds()
        )

        # Prevent negative time
        if total_seconds < 0:

            total_seconds = 0

        hours = total_seconds // 3600

        minutes = (
            total_seconds % 3600
        ) // 60

        seconds = (
            total_seconds % 60
        )

        total_hours = (
            f"{hours}h "
            f"{minutes}m "
            f"{seconds}s"
        )

        # ----------------------------------------------------
        # SAVE CLOCK OUT
        # ----------------------------------------------------

        database.clock_out_employee(
            attendance_id,
            clock_out_string,
            total_hours
        )

        messagebox.showinfo(
            "Clock Out Successful",
            f"{employee_name} has successfully clocked out.\n\n"
            f"Time Worked:\n"
            f"{total_hours}"
        )

        self.clear_employee_id()

        self.load_today()

    # ========================================================
    # LOAD TODAY
    # ========================================================

    def load_today(self):

        self.clear_table()

        records = database.get_today_attendance()

        self.insert_records(
            records
        )

    # ========================================================
    # LOAD ALL
    # ========================================================

    def load_all(self):

        self.clear_table()

        records = database.get_all_attendance()

        self.insert_records(
            records
        )

    # ========================================================
    # SEARCH
    # ========================================================

    def search_attendance(self):

        search_text = (
            self.search_entry
            .get()
            .strip()
        )

        if not search_text:

            self.load_today()

            return

        self.clear_table()

        records = database.search_attendance(
            search_text
        )

        self.insert_records(
            records
        )

    # ========================================================
    # INSERT RECORDS
    # ========================================================

    def insert_records(self, records):

        for record in records:

            employee_id = record[0]
            employee_name = record[1]
            clock_in = record[2]
            clock_out = record[3]
            total_hours = record[4]

            if clock_out:

                status = "Clocked Out"

            else:

                status = "Working"

            self.attendance_table.insert(
                "",
                "end",
                values=(
                    employee_id,
                    employee_name,
                    clock_in,
                    clock_out or "-",
                    total_hours or "-",
                    status
                )
            )

    # ========================================================
    # CLEAR TABLE
    # ========================================================

    def clear_table(self):

        for item in self.attendance_table.get_children():

            self.attendance_table.delete(
                item
            )

    # ========================================================
    # CLEAR EMPLOYEE ID
    # ========================================================

    def clear_employee_id(self):

        self.employee_id_entry.delete(
            0,
            "end"
        )

        self.employee_id_entry.focus()

    # ========================================================
    # REFRESH
    # ========================================================

    def refresh(self):

        self.load_today()
