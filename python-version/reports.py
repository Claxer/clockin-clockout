import customtkinter as ctk
from tkinter import messagebox, filedialog
from datetime import datetime
import csv

from database import (
    get_attendance,
    get_monthly_summary,
    get_employee_summary,
    get_all_employees
)


class ReportsPage(ctk.CTkFrame):
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

        self.create_ui()

        self.load_report()

    # =====================================================
    # UI
    # =====================================================

    def create_ui(self):
        title = ctk.CTkLabel(
            self,
            text="Attendance Reports",
            font=("Arial", 30, "bold")
        )

        title.grid(
            row=0,
            column=0,
            sticky="w",
            pady=(0, 20)
        )

        controls = ctk.CTkFrame(
            self
        )

        controls.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=(0, 15)
        )

        ctk.CTkLabel(
            controls,
            text="Year:"
        ).pack(
            side="left",
            padx=(15, 5),
            pady=15
        )

        self.year = ctk.CTkEntry(
            controls,
            width=100
        )

        self.year.pack(
            side="left",
            padx=5
        )

        self.year.insert(
            0,
            str(datetime.now().year)
        )

        ctk.CTkLabel(
            controls,
            text="Month:"
        ).pack(
            side="left",
            padx=(15, 5)
        )

        self.month = ctk.CTkComboBox(
            controls,
            values=[
                "1", "2", "3", "4",
                "5", "6", "7", "8",
                "9", "10", "11", "12"
            ],
            width=80
        )

        self.month.pack(
            side="left",
            padx=5
        )

        self.month.set(
            str(datetime.now().month)
        )

        ctk.CTkButton(
            controls,
            text="GENERATE",
            command=self.load_report
        ).pack(
            side="left",
            padx=10
        )

        ctk.CTkButton(
            controls,
            text="EXPORT CSV",
            command=self.export_csv
        ).pack(
            side="right",
            padx=15
        )

        self.summary_frame = ctk.CTkFrame(
            self
        )

        self.summary_frame.grid(
            row=2,
            column=0,
            sticky="ew",
            pady=(0, 15)
        )

        self.report_area = ctk.CTkScrollableFrame(
            self
        )

        self.report_area.grid(
            row=3,
            column=0,
            sticky="nsew"
        )

    # =====================================================
    # REPORT
    # =====================================================

    def load_report(self):
        for widget in self.summary_frame.winfo_children():
            widget.destroy()

        for widget in self.report_area.winfo_children():
            widget.destroy()

        try:
            year = int(
                self.year.get()
            )

            month = int(
                self.month.get()
            )

        except ValueError:
            messagebox.showerror(
                "Invalid Date",
                "Please enter a valid year and month."
            )

            return

        summary = get_monthly_summary(
            year,
            month
        )

        cards = [
            (
                "Attendance Records",
                summary["total_records"]
            ),
            (
                "Total Hours",
                f"{summary['total_hours']:.2f}"
            ),
            (
                "Overtime Hours",
                f"{summary['overtime_hours']:.2f}"
            )
        ]

        for index, (label, value) in enumerate(cards):
            self.summary_frame.grid_columnconfigure(
                index,
                weight=1
            )

            card = ctk.CTkFrame(
                self.summary_frame
            )

            card.grid(
                row=0,
                column=index,
                sticky="ew",
                padx=5,
                pady=5
            )

            ctk.CTkLabel(
                card,
                text=str(value),
                font=("Arial", 25, "bold")
            ).pack(
                pady=(15, 5)
            )

            ctk.CTkLabel(
                card,
                text=label,
                text_color="gray"
            ).pack(
                pady=(0, 15)
            )

        records = get_attendance(
            selected_date=""
        )

        month_records = [
            record
            for record in records
            if record["date"].startswith(
                f"{year}-{month:02d}-"
            )
        ]

        title = ctk.CTkLabel(
            self.report_area,
            text=f"Employee Summary - {year}-{month:02d}",
            font=("Arial", 20, "bold")
        )

        title.pack(
            anchor="w",
            pady=(10, 20)
        )

        employees = get_all_employees()

        for employee in employees:
            employee_summary = get_employee_summary(
                employee["employee_id"]
            )

            employee_records = [
                record
                for record in month_records
                if record["employee_id"]
                == employee["employee_id"]
            ]

            if not employee_records:
                continue

            card = ctk.CTkFrame(
                self.report_area
            )

            card.pack(
                fill="x",
                pady=5
            )

            ctk.CTkLabel(
                card,
                text=(
                    f"{employee['employee_id']}  |  "
                    f"{employee['name']}"
                ),
                font=("Arial", 14, "bold")
            ).pack(
                anchor="w",
                padx=15,
                pady=(12, 5)
            )

            ctk.CTkLabel(
                card,
                text=(
                    f"Department: {employee['department']}    "
                    f"Position: {employee['position']}"
                ),
                text_color="gray"
            ).pack(
                anchor="w",
                padx=15
            )

            ctk.CTkLabel(
                card,
                text=(
                    f"Days Recorded: {len(employee_records)}    "
                    f"Total Hours: "
                    f"{sum((r['total_hours'] or 0) for r in employee_records):.2f}    "
                    f"Overtime: "
                    f"{sum((r['overtime_hours'] or 0) for r in employee_records):.2f}"
                )
            ).pack(
                anchor="w",
                padx=15,
                pady=(5, 12)
            )

        if not month_records:
            ctk.CTkLabel(
                self.report_area,
                text="No records found for this month.",
                text_color="gray"
            ).pack(
                pady=30
            )

    # =====================================================
    # EXPORT CSV
    # =====================================================

    def export_csv(self):
        try:
            year = int(
                self.year.get()
            )

            month = int(
                self.month.get()
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Invalid year or month."
            )

            return

        records = get_attendance()

        month_records = [
            record
            for record in records
            if record["date"].startswith(
                f"{year}-{month:02d}-"
            )
        ]

        if not month_records:
            messagebox.showwarning(
                "No Data",
                "There are no attendance records to export."
            )

            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[
                (
                    "CSV Files",
                    "*.csv"
                )
            ],
            initialfile=(
                f"attendance_{year}_{month:02d}.csv"
            )
        )

        if not file_path:
            return

        with open(
            file_path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(
                file
            )

            writer.writerow([
                "Employee ID",
                "Name",
                "Department",
                "Position",
                "Date",
                "Clock In",
                "Clock Out",
                "Total Hours",
                "Overtime Hours",
                "Status",
                "Remarks"
            ])

            for record in month_records:
                writer.writerow([
                    record["employee_id"],
                    record["name"],
                    record["department"],
                    record["position"],
                    record["date"],
                    record["clock_in"],
                    record["clock_out"],
                    record["total_hours"],
                    record["overtime_hours"],
                    record["status"],
                    record["remarks"]
                ])

        messagebox.showinfo(
            "Export Complete",
            "Attendance report exported successfully."
        )
