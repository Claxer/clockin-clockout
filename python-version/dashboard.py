import customtkinter as ctk
from tkinter import ttk, messagebox
from datetime import datetime

import database


class DashboardPage:

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
        self.orange = "#FF9500"
        self.red = "#FF3B30"

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

        self.create_header()

        self.create_statistics()

        self.create_quick_attendance()

        self.create_recent_attendance()

    # ========================================================
    # HEADER
    # ========================================================

    def create_header(self):

        header = ctk.CTkFrame(
            self.frame,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            padx=30,
            pady=(25, 10)
        )

        # ----------------------------------------------------
        # LEFT SIDE
        # ----------------------------------------------------

        left = ctk.CTkFrame(
            header,
            fg_color="transparent"
        )

        left.pack(
            side="left"
        )

        self.title_label = ctk.CTkLabel(
            left,
            text="Dashboard",
            font=ctk.CTkFont(
                size=28,
                weight="bold"
            ),
            text_color=self.text_color
        )

        self.title_label.pack(
            anchor="w"
        )

        subtitle = ctk.CTkLabel(
            left,
            text="Company attendance overview",
            font=ctk.CTkFont(
                size=13
            ),
            text_color=self.secondary_text
        )

        subtitle.pack(
            anchor="w"
        )

        # ----------------------------------------------------
        # RIGHT SIDE - DATE AND TIME
        # ----------------------------------------------------

        right = ctk.CTkFrame(
            header,
            fg_color="transparent"
        )

        right.pack(
            side="right"
        )

        self.date_label = ctk.CTkLabel(
            right,
            text="",
            font=ctk.CTkFont(
                size=13,
                weight="bold"
            ),
            text_color=self.text_color
        )

        self.date_label.pack(
            anchor="e"
        )

        self.time_label = ctk.CTkLabel(
            right,
            text="",
            font=ctk.CTkFont(
                size=12
            ),
            text_color=self.secondary_text
        )

        self.time_label.pack(
            anchor="e"
        )

        self.update_clock()

    # ========================================================
    # LIVE CLOCK
    # ========================================================

    def update_clock(self):

        current_time = datetime.now()

        date_text = current_time.strftime(
            "%A, %B %d, %Y"
        )

        time_text = current_time.strftime(
            "%I:%M:%S %p"
        )

        self.date_label.configure(
            text=date_text
        )

        self.time_label.configure(
            text=time_text
        )

        self.frame.after(
            1000,
            self.update_clock
        )

    # ========================================================
    # STATISTICS
    # ========================================================

    def create_statistics(self):

        stats_frame = ctk.CTkFrame(
            self.frame,
            fg_color="transparent"
        )

        stats_frame.pack(
            fill="x",
            padx=25,
            pady=(5, 15)
        )

        # ----------------------------------------------------
        # TOTAL EMPLOYEES
        # ----------------------------------------------------

        self.total_card = self.create_stat_card(
            stats_frame,
            "Total Employees",
            "0",
            self.blue
        )

        # ----------------------------------------------------
        # CURRENTLY WORKING
        # ----------------------------------------------------

        self.working_card = self.create_stat_card(
            stats_frame,
            "Currently Working",
            "0",
            self.green
        )

        # ----------------------------------------------------
        # CLOCKED OUT
        # ----------------------------------------------------

        self.clocked_out_card = self.create_stat_card(
            stats_frame,
            "Clocked Out",
            "0",
            self.orange
        )

        # ----------------------------------------------------
        # TODAY'S RECORDS
        # ----------------------------------------------------

        self.records_card = self.create_stat_card(
            stats_frame,
            "Today's Records",
            "0",
            self.blue
        )

        self.refresh_statistics()

    # ========================================================
    # STAT CARD
    # ========================================================

    def create_stat_card(
        self,
        parent,
        title,
        value,
        accent
    ):

        card = ctk.CTkFrame(
            parent,
            height=115,
            fg_color=self.card_color,
            corner_radius=15,
            border_width=1,
            border_color=self.border
        )

        card.pack(
            side="left",
            fill="x",
            expand=True,
            padx=5
        )

        # ----------------------------------------------------
        # ACCENT
        # ----------------------------------------------------

        accent_bar = ctk.CTkFrame(
            card,
            width=5,
            fg_color=accent,
            corner_radius=3
        )

        accent_bar.pack(
            side="left",
            fill="y",
            padx=(15, 12),
            pady=20
        )

        # ----------------------------------------------------
        # TEXT
        # ----------------------------------------------------

        text_frame = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        text_frame.pack(
            side="left",
            fill="both",
            expand=True
        )

        title_label = ctk.CTkLabel(
            text_frame,
            text=title,
            font=ctk.CTkFont(
                size=12
            ),
            text_color=self.secondary_text
        )

        title_label.pack(
            anchor="w",
            pady=(22, 0)
        )

        value_label = ctk.CTkLabel(
            text_frame,
            text=value,
            font=ctk.CTkFont(
                size=27,
                weight="bold"
            ),
            text_color=self.text_color
        )

        value_label.pack(
            anchor="w"
        )

        return value_label

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
            pady=(0, 15)
        )

        # ----------------------------------------------------
        # TITLE
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
            text="Enter an employee ID to quickly record attendance.",
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
        # INPUT
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
        # CLOCK IN
        # ----------------------------------------------------

        clock_in_button = ctk.CTkButton(
            input_frame,
            text="Clock In",
            width=120,
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
        # CLOCK OUT
        # ----------------------------------------------------

        clock_out_button = ctk.CTkButton(
            input_frame,
            text="Clock Out",
            width=120,
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
        # CLEAR
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
            command=self.clear_entry
        )

        clear_button.pack(
            side="left",
            padx=5
        )

    # ========================================================
    # RECENT ATTENDANCE
    # ========================================================

    def create_recent_attendance(self):

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
            text="Today's Attendance",
            font=ctk.CTkFont(
                size=18,
                weight="bold"
            ),
            text_color=self.text_color
        )

        title.pack(
            side="left"
        )

        refresh_button = ctk.CTkButton(
            title_frame,
            text="Refresh",
            width=90,
            height=36,
            corner_radius=8,
            fg_color="#E5E5E7",
            hover_color="#D5D5D7",
            text_color=self.text_color,
            command=self.refresh
        )

        refresh_button.pack(
            side="right"
        )

        # ----------------------------------------------------
        # TABLE CARD
        # ----------------------------------------------------

        table_card = ctk.CTkFrame(
            self.frame,
            fg_color=self.card_color,
            corner_radius=15,
            border_width=1,
            border_color=self.border
        )

        table_card.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(5, 20)
        )

        self.create_table(
            table_card
        )

    # ========================================================
    # CREATE TABLE
    # ========================================================

    def create_table(self, parent):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "Dashboard.Treeview",
            rowheight=38,
            font=("Segoe UI", 10),
            background="#FFFFFF",
            fieldbackground="#FFFFFF",
            borderwidth=0
        )

        style.configure(
            "Dashboard.Treeview.Heading",
            font=("Segoe UI", 10, "bold"),
            background="#F0F0F2",
            foreground="#1D1D1F",
            padding=8
        )

        style.map(
            "Dashboard.Treeview",
            background=[
                ("selected", "#DCEBFA")
            ],
            foreground=[
                ("selected", "#1D1D1F")
            ]
        )

        self.attendance_table = ttk.Treeview(
            parent,
            columns=(
                "employee_id",
                "name",
                "clock_in",
                "clock_out",
                "hours",
                "status"
            ),
            show="headings",
            style="Dashboard.Treeview"
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
            width=190
        )

        self.attendance_table.column(
            "clock_in",
            width=160
        )

        self.attendance_table.column(
            "clock_out",
            width=160
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

        self.attendance_table.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.load_today_attendance()

    # ========================================================
    # LOAD TODAY'S ATTENDANCE
    # ========================================================

    def load_today_attendance(self):

        self.clear_table()

        records = database.get_today_attendance()

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

        employee = database.get_employee(
            employee_id
        )

        if not employee:

            messagebox.showerror(
                "Employee Not Found",
                "This employee ID is not registered."
            )

            return

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

        current_time = datetime.now()

        clock_in_time = (
            current_time.strftime(
                "%Y-%m-%d %I:%M:%S %p"
            )
        )

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

        self.clear_entry()

        self.refresh()

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

        active_record = (
            database.get_active_attendance(
                employee_id
            )
        )

        if not active_record:

            messagebox.showwarning(
                "Not Clocked In",
                "This employee is not currently clocked in."
            )

            return

        attendance_id = active_record[0]
        employee_name = active_record[2]
        clock_in_string = active_record[3]

        try:

            clock_in_time = datetime.strptime(
                clock_in_string,
                "%Y-%m-%d %I:%M:%S %p"
            )

        except ValueError:

            messagebox.showerror(
                "Time Error",
                "The saved clock-in time could not be read."
            )

            return

        clock_out_time = datetime.now()

        clock_out_string = (
            clock_out_time.strftime(
                "%Y-%m-%d %I:%M:%S %p"
            )
        )

        difference = (
            clock_out_time - clock_in_time
        )

        total_seconds = int(
            difference.total_seconds()
        )

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

        database.clock_out_employee(
            attendance_id,
            clock_out_string,
            total_hours
        )

        messagebox.showinfo(
            "Clock Out Successful",
            f"{employee_name} has successfully clocked out.\n\n"
            f"Total Working Time:\n"
            f"{total_hours}"
        )

        self.clear_entry()

        self.refresh()

    # ========================================================
    # CLEAR ENTRY
    # ========================================================

    def clear_entry(self):

        self.employee_id_entry.delete(
            0,
            "end"
        )

        self.employee_id_entry.focus()

    # ========================================================
    # CLEAR TABLE
    # ========================================================

    def clear_table(self):

        for item in self.attendance_table.get_children():

            self.attendance_table.delete(
                item
            )

    # ========================================================
    # REFRESH DASHBOARD
    # ========================================================

    def refresh(self):

        self.refresh_statistics()

        self.load_today_attendance()

    # ========================================================
    # REFRESH STATISTICS
    # ========================================================

    def refresh_statistics(self):

        total_employees = (
            database.get_employee_count()
        )

        currently_working = (
            database.get_clocked_in_count()
        )

        today_records = (
            database.get_today_attendance()
        )

        today_record_count = len(
            today_records
        )

        # ----------------------------------------------------
        # CLOCKED OUT TODAY
        # ----------------------------------------------------

        clocked_out_today = 0

        for record in today_records:

            if record[3]:

                clocked_out_today += 1

        # ----------------------------------------------------
        # UPDATE CARDS
        # ----------------------------------------------------

        self.total_card.configure(
            text=str(total_employees)
        )

        self.working_card.configure(
            text=str(currently_working)
        )

        self.clocked_out_card.configure(
            text=str(clocked_out_today)
        )

        self.records_card.configure(
            text=str(today_record_count)
        )
