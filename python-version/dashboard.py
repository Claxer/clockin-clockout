import customtkinter as ctk
from datetime import datetime

from database import (
    get_dashboard_stats,
    get_today_attendance
)


class DashboardPage(ctk.CTkFrame):
    def __init__(self, parent, open_attendance):
        super().__init__(parent)

        self.open_attendance = open_attendance

        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.grid_rowconfigure(
            3,
            weight=1
        )

        self.create_ui()

        self.update_dashboard()
        self.update_clock()

    # =====================================================
    # UI
    # =====================================================

    def create_ui(self):
        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 32, "bold")
        )

        title.grid(
            row=0,
            column=0,
            sticky="w"
        )

        self.clock_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 16)
        )

        self.clock_label.grid(
            row=1,
            column=0,
            sticky="w",
            pady=(5, 20)
        )

        self.create_stat_cards()

        self.create_recent_section()

    def create_stat_cards(self):
        self.stats_frame = ctk.CTkFrame(
            self
        )

        self.stats_frame.grid(
            row=2,
            column=0,
            sticky="ew",
            pady=(0, 20)
        )

        for i in range(6):
            self.stats_frame.grid_columnconfigure(
                i,
                weight=1
            )

        self.stat_values = []

        labels = [
            "Employees",
            "Working Now",
            "Today's Records",
            "Completed",
            "Hours Today",
            "Late Today"
        ]

        for index, label in enumerate(labels):
            card = ctk.CTkFrame(
                self.stats_frame,
                height=120
            )

            card.grid(
                row=0,
                column=index,
                sticky="nsew",
                padx=5,
                pady=5
            )

            card.grid_propagate(False)

            value = ctk.CTkLabel(
                card,
                text="0",
                font=("Arial", 28, "bold")
            )

            value.pack(
                pady=(20, 5)
            )

            ctk.CTkLabel(
                card,
                text=label,
                font=("Arial", 12),
                text_color="gray"
            ).pack()

            self.stat_values.append(
                value
            )

    def create_recent_section(self):
        self.recent_frame = ctk.CTkFrame(
            self
        )

        self.recent_frame.grid(
            row=3,
            column=0,
            sticky="nsew"
        )

        self.recent_frame.grid_columnconfigure(
            0,
            weight=1
        )

        self.recent_frame.grid_rowconfigure(
            1,
            weight=1
        )

        header = ctk.CTkFrame(
            self.recent_frame,
            fg_color="transparent"
        )

        header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=15,
            pady=15
        )

        ctk.CTkLabel(
            header,
            text="Today's Attendance",
            font=("Arial", 20, "bold")
        ).pack(
            side="left"
        )

        ctk.CTkButton(
            header,
            text="Open Attendance",
            width=140,
            command=self.open_attendance
        ).pack(
            side="right"
        )

        self.records_frame = ctk.CTkScrollableFrame(
            self.recent_frame
        )

        self.records_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=15,
            pady=(0, 15)
        )

    # =====================================================
    # UPDATE
    # =====================================================

    def update_dashboard(self):
        stats = get_dashboard_stats()

        values = [
            stats["total_employees"],
            stats["currently_working"],
            stats["today_records"],
            stats["completed"],
            f"{stats['total_hours']:.2f}",
            stats["late_count"]
        ]

        for label, value in zip(
            self.stat_values,
            values
        ):
            label.configure(
                text=str(value)
            )

        self.load_recent_attendance()

    def load_recent_attendance(self):
        for widget in self.records_frame.winfo_children():
            widget.destroy()

        records = get_today_attendance()

        if not records:
            ctk.CTkLabel(
                self.records_frame,
                text="No attendance records for today.",
                text_color="gray"
            ).pack(
                pady=30
            )

            return

        headers = [
            "Employee ID",
            "Name",
            "Department",
            "Clock In",
            "Clock Out",
            "Hours",
            "Status"
        ]

        header = ctk.CTkFrame(
            self.records_frame
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

        for record in records:
            row = ctk.CTkFrame(
                self.records_frame
            )

            row.pack(
                fill="x",
                pady=2
            )

            values = [
                record["employee_id"],
                record["name"],
                record["department"],
                self.format_time(record["clock_in"]),
                self.format_time(record["clock_out"]),
                (
                    f"{record['total_hours']:.2f}"
                    if record["total_hours"]
                    else "--"
                ),
                record["status"]
            ]

            for value in values:
                ctk.CTkLabel(
                    row,
                    text=value,
                    font=("Arial", 11)
                ).pack(
                    side="left",
                    expand=True,
                    fill="x",
                    pady=8
                )

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
