import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

from database import (
    clock_employee_in,
    clock_employee_out,
    get_attendance
)


class AttendancePage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.grid_rowconfigure(
            4,
            weight=1
        )

        self.create_ui()

        self.load_attendance()

    # =====================================================
    # UI
    # =====================================================

    def create_ui(self):
        title = ctk.CTkLabel(
            self,
            text="Employee Attendance",
            font=("Arial", 30, "bold")
        )

        title.grid(
            row=0,
            column=0,
            sticky="w",
            pady=(0, 20)
        )

        self.clock_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 18, "bold")
        )

        self.clock_label.grid(
            row=1,
            column=0,
            sticky="w",
            pady=(0, 15)
        )

        self.update_clock()

        # Clock actions
        clock_frame = ctk.CTkFrame(
            self
        )

        clock_frame.grid(
            row=2,
            column=0,
            sticky="ew",
            pady=(0, 15)
        )

        self.employee_id = ctk.CTkEntry(
            clock_frame,
            placeholder_text="Enter Employee ID",
            height=45
        )

        self.employee_id.pack(
            side="left",
            padx=15,
            pady=15
        )

        ctk.CTkButton(
            clock_frame,
            text="CLOCK IN",
            height=45,
            command=self.clock_in
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            clock_frame,
            text="CLOCK OUT",
            height=45,
            command=self.clock_out
        ).pack(
            side="left",
            padx=5
        )

        # Filters
        filters = ctk.CTkFrame(
            self
        )

        filters.grid(
            row=3,
            column=0,
            sticky="ew",
            pady=(0, 15)
        )

        filters.grid_columnconfigure(
            0,
            weight=1
        )

        self.search = ctk.CTkEntry(
            filters,
            placeholder_text="Search ID, name, or department..."
        )

        self.search.grid(
            row=0,
            column=0,
            padx=8,
            pady=10,
            sticky="ew"
        )

        self.search.bind(
            "<KeyRelease>",
            lambda event: self.load_attendance()
        )

        self.date_filter = ctk.CTkEntry(
            filters,
            placeholder_text="Date YYYY-MM-DD"
        )

        self.date_filter.grid(
            row=0,
            column=1,
            padx=8,
            pady=10
        )

        self.status_filter = ctk.CTkComboBox(
            filters,
            values=[
                "All",
                "Present",
                "Late"
            ],
            width=130
        )

        self.status_filter.set(
            "All"
        )

        self.status_filter.grid(
            row=0,
            column=2,
            padx=8,
            pady=10
        )

        ctk.CTkButton(
            filters,
            text="FILTER",
            width=100,
            command=self.load_attendance
        ).grid(
            row=0,
            column=3,
            padx=8,
            pady=10
        )

        ctk.CTkButton(
            filters,
            text="TODAY",
            width=100,
            command=self.show_today
        ).grid(
            row=0,
            column=4,
            padx=8,
            pady=10
        )

        ctk.CTkButton(
            filters,
            text="CLEAR",
            width=100,
            command=self.clear_filters
        ).grid(
            row=0,
            column=5,
            padx=8,
            pady=10
        )

        self.log = ctk.CTkScrollableFrame(
            self
        )

        self.log.grid(
            row=4,
            column=0,
            sticky="nsew"
        )

    # =====================================================
    # CLOCK IN
    # =====================================================

    def clock_in(self):
        employee_id = self.employee_id.get().strip()

        if not employee_id:
            messagebox.showwarning(
                "Missing ID",
                "Enter an employee ID."
            )

            return

        success, message = clock_employee_in(
            employee_id
        )

        if success:
            messagebox.showinfo(
                "Clock In",
                message
            )

            self.employee_id.delete(
                0,
                "end"
            )

            self.load_attendance()

        else:
            messagebox.showwarning(
                "Clock In",
                message
            )

    # =====================================================
    # CLOCK OUT
    # =====================================================

    def clock_out(self):
        employee_id = self.employee_id.get().strip()

        if not employee_id:
            messagebox.showwarning(
                "Missing ID",
                "Enter an employee ID."
            )

            return

        success, message, hours = clock_employee_out(
            employee_id
        )

        if success:
            messagebox.showinfo(
                "Clock Out",
                f"{message}\n\n"
                f"Hours Worked: {hours:.2f} hours"
            )

            self.employee_id.delete(
                0,
                "end"
            )

            self.load_attendance()

        else:
            messagebox.showwarning(
                "Clock Out",
                message
            )

    # =====================================================
    # LOAD
    # =====================================================

    def load_attendance(self):
        for widget in self.log.winfo_children():
            widget.destroy()

        search = self.search.get().strip()
        selected_date = self.date_filter.get().strip()
        status = self.status_filter.get()

        records = get_attendance(
            search,
            selected_date,
            status
        )

        if not records:
            ctk.CTkLabel(
                self.log,
                text="No attendance records found.",
                text_color="gray"
            ).pack(
                pady=30
            )

            return

        headers = [
            "ID",
            "Employee",
            "Name",
            "Date",
            "Clock In",
            "Clock Out",
            "Hours",
            "OT",
            "Status"
        ]

        header = ctk.CTkFrame(
            self.log
        )

        header.pack(
            fill="x",
            pady=(0, 5)
        )

        for text in headers:
            ctk.CTkLabel(
                header,
                text=text,
                font=("Arial", 11, "bold")
            ).pack(
                side="left",
                expand=True,
                fill="x",
                pady=10
            )

        for record in records:
            row = ctk.CTkFrame(
                self.log
            )

            row.pack(
                fill="x",
                pady=2
            )

            values = [
                record["id"],
                record["employee_id"],
                record["name"],
                record["date"],
                self.format_time(
                    record["clock_in"]
                ),
                self.format_time(
                    record["clock_out"]
                ),
                (
                    f"{record['total_hours']:.2f}"
                    if record["total_hours"]
                    else "--"
                ),
                (
                    f"{record['overtime_hours']:.2f}"
                    if record["overtime_hours"]
                    else "--"
                ),
                record["status"]
            ]

            for value in values:
                ctk.CTkLabel(
                    row,
                    text=str(value),
                    font=("Arial", 10)
                ).pack(
                    side="left",
                    expand=True,
                    fill="x",
                    pady=8
                )

    # =====================================================
    # FILTER HELPERS
    # =====================================================

    def show_today(self):
        today = datetime.now().strftime(
            "%Y-%m-%d"
        )

        self.date_filter.delete(
            0,
            "end"
        )

        self.date_filter.insert(
            0,
            today
        )

        self.load_attendance()

    def clear_filters(self):
        self.search.delete(
            0,
            "end"
        )

        self.date_filter.delete(
            0,
            "end"
        )

        self.status_filter.set(
            "All"
        )

        self.load_attendance()

    # =====================================================
    # LIVE CLOCK
    # =====================================================

    def update_clock(self):
        now = datetime.now()

        self.clock_label.configure(
            text=now.strftime(
                "%A, %B %d, %Y  |  %I:%M:%S %p"
            )
        )

        self.after(
            1000,
            self.update_clock
        )

    # =====================================================
    # TIME FORMAT
    # =====================================================

    def format_time(self, value):
        if not value:
            return "--"

        try:
            time = datetime.strptime(
                value,
                "%H:%M:%S"
            )

            return time.strftime(
                "%I:%M %p"
            )

        except ValueError:
            return value
