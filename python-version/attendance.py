import customtkinter as ctk
from tkinter import messagebox

import database


class AttendancePage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.create_header()
        self.create_filters()
        self.create_table()

        self.refresh_attendance()

    def create_header(self):
        header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        header.pack(
            fill="x",
            padx=25,
            pady=(20, 10)
        )

        title = ctk.CTkLabel(
            header,
            text="Attendance",
            font=ctk.CTkFont(
                size=28,
                weight="bold"
            )
        )
        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            header,
            text="View and manage employee attendance records.",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitle.pack(anchor="w", pady=(3, 0))

    def create_filters(self):
        filter_frame = ctk.CTkFrame(
            self,
            corner_radius=12
        )
        filter_frame.pack(
            fill="x",
            padx=25,
            pady=10
        )

        self.search_entry = ctk.CTkEntry(
            filter_frame,
            placeholder_text="Search employee...",
            width=220,
            height=38
        )
        self.search_entry.pack(
            side="left",
            padx=(15, 8),
            pady=15
        )

        self.start_date_entry = ctk.CTkEntry(
            filter_frame,
            placeholder_text="Start Date YYYY-MM-DD",
            width=160,
            height=38
        )
        self.start_date_entry.pack(
            side="left",
            padx=8,
            pady=15
        )

        self.end_date_entry = ctk.CTkEntry(
            filter_frame,
            placeholder_text="End Date YYYY-MM-DD",
            width=160,
            height=38
        )
        self.end_date_entry.pack(
            side="left",
            padx=8,
            pady=15
        )

        search_button = ctk.CTkButton(
            filter_frame,
            text="Search",
            width=90,
            height=38,
            command=self.refresh_attendance
        )
        search_button.pack(
            side="left",
            padx=8,
            pady=15
        )

        clear_button = ctk.CTkButton(
            filter_frame,
            text="Clear",
            width=80,
            height=38,
            fg_color="gray",
            hover_color="#555555",
            command=self.clear_filters
        )
        clear_button.pack(
            side="left",
            padx=8,
            pady=15
        )

    def create_table(self):
        table_frame = ctk.CTkFrame(
            self,
            corner_radius=12
        )
        table_frame.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(5, 25)
        )

        self.table = ctk.CTkScrollableFrame(
            table_frame,
            fg_color="transparent"
        )
        self.table.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.create_table_headers()

    def create_table_headers(self):
        headers = [
            "Employee ID",
            "Employee Name",
            "Department",
            "Date",
            "Clock In",
            "Clock Out",
            "Hours",
            "Status"
        ]

        widths = [
            120,
            180,
            130,
            110,
            100,
            100,
            80,
            100
        ]

        for column, (header, width) in enumerate(
            zip(headers, widths)
        ):
            label = ctk.CTkLabel(
                self.table,
                text=header,
                width=width,
                font=ctk.CTkFont(
                    size=13,
                    weight="bold"
                ),
                anchor="w"
            )

            label.grid(
                row=0,
                column=column,
                padx=5,
                pady=(5, 10),
                sticky="w"
            )

    def refresh_attendance(self):
        search = self.search_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()

        records = database.get_attendance(
            search=search,
            start_date=start_date,
            end_date=end_date
        )

        self.display_records(records)

    def display_records(self, records):
        for widget in self.table.winfo_children():
            if widget.grid_info().get("row", 0) != 0:
                widget.destroy()

        if not records:
            empty_label = ctk.CTkLabel(
                self.table,
                text="No attendance records found.",
                text_color="gray",
                font=ctk.CTkFont(size=14)
            )

            empty_label.grid(
                row=1,
                column=0,
                columnspan=8,
                pady=40
            )

            return

        for row_number, record in enumerate(
            records,
            start=1
        ):
            values = [
                record["employee_id"],
                record["full_name"],
                record["department"],
                record["work_date"],
                record["clock_in"],
                record["clock_out"] or "-",
                f'{record["total_hours"]:.2f}',
                record["status"]
            ]

            for column, value in enumerate(values):

                label = ctk.CTkLabel(
                    self.table,
                    text=str(value),
                    width=[
                        120,
                        180,
                        130,
                        110,
                        100,
                        100,
                        80,
                        100
                    ][column],
                    anchor="w"
                )

                label.grid(
                    row=row_number,
                    column=column,
                    padx=5,
                    pady=7,
                    sticky="w"
                )

    def clear_filters(self):
        self.search_entry.delete(0, "end")
        self.start_date_entry.delete(0, "end")
        self.end_date_entry.delete(0, "end")

        self.refresh_attendance()
