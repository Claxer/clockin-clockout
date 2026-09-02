import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

from database import connect_db


class AttendancePage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

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
            pady=(10, 20)
        )

        # Clock section
        clock_frame = ctk.CTkFrame(self)

        clock_frame.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        self.employee_id = ctk.CTkEntry(
            clock_frame,
            placeholder_text="Enter Employee ID",
            height=45
        )

        self.employee_id.pack(
            side="left",
            padx=15,
            pady=20
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

        # Search
        self.search = ctk.CTkEntry(
            self,
            placeholder_text="Search attendance..."
        )

        self.search.grid(
            row=2,
            column=0,
            sticky="ew",
            pady=15
        )

        self.search.bind(
            "<KeyRelease>",
            lambda event: self.load_attendance()
        )

        # Attendance log
        self.log = ctk.CTkScrollableFrame(
            self
        )

        self.log.grid(
            row=3,
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

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT name
            FROM employees
            WHERE employee_id = ?
        """, (employee_id,))

        employee = cursor.fetchone()

        if not employee:

            conn.close()

            messagebox.showerror(
                "Error",
                "Employee not found."
            )

            return

        today = datetime.now().strftime(
            "%Y-%m-%d"
        )

        # Check active clock in
        cursor.execute("""
            SELECT id
            FROM attendance
            WHERE employee_id = ?
            AND date = ?
            AND clock_out IS NULL
        """, (
            employee_id,
            today
        ))

        if cursor.fetchone():

            conn.close()

            messagebox.showwarning(
                "Already Clocked In",
                f"{employee[0]} is already clocked in."
            )

            return

        now = datetime.now()

        cursor.execute("""
            INSERT INTO attendance
            (
                employee_id,
                date,
                clock_in
            )
            VALUES (?, ?, ?)
        """, (
            employee_id,
            today,
            now.strftime("%H:%M:%S")
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Clock In",
            f"{employee[0]} clocked in.\n\n"
            f"Time: {now.strftime('%I:%M:%S %p')}"
        )

        self.load_attendance()

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

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT name
            FROM employees
            WHERE employee_id = ?
        """, (employee_id,))

        employee = cursor.fetchone()

        if not employee:

            conn.close()

            messagebox.showerror(
                "Error",
                "Employee not found."
            )

            return

        today = datetime.now().strftime(
            "%Y-%m-%d"
        )

        cursor.execute("""
            SELECT id, clock_in
            FROM attendance
            WHERE employee_id = ?
            AND date = ?
            AND clock_out IS NULL
            ORDER BY id DESC
            LIMIT 1
        """, (
            employee_id,
            today
        ))

        record = cursor.fetchone()

        if not record:

            conn.close()

            messagebox.showwarning(
                "Not Clocked In",
                f"{employee[0]} is not clocked in."
            )

            return

        record_id = record[0]
        clock_in = record[1]

        now = datetime.now()

        clock_in_datetime = datetime.strptime(
            f"{today} {clock_in}",
            "%Y-%m-%d %H:%M:%S"
        )

        difference = now - clock_in_datetime

        total_hours = (
            difference.total_seconds() / 3600
        )

        cursor.execute("""
            UPDATE attendance
            SET clock_out = ?,
                total_hours = ?
            WHERE id = ?
        """, (
            now.strftime("%H:%M:%S"),
            round(total_hours, 2),
            record_id
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Clock Out",
            f"{employee[0]} clocked out.\n\n"
            f"Time: {now.strftime('%I:%M:%S %p')}\n"
            f"Hours Worked: {total_hours:.2f}"
        )

        self.load_attendance()

    # =====================================================
    # LOAD ATTENDANCE
    # =====================================================

    def load_attendance(self):

        for widget in self.log.winfo_children():
            widget.destroy()

        search = self.search.get().strip()

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                attendance.employee_id,
                employees.name,
                employees.department,
                attendance.date,
                attendance.clock_in,
                attendance.clock_out,
                attendance.total_hours

            FROM attendance

            JOIN employees
            ON attendance.employee_id =
               employees.employee_id

            WHERE attendance.employee_id LIKE ?
            OR employees.name LIKE ?

            ORDER BY attendance.id DESC
        """, (
            f"%{search}%",
            f"%{search}%"
        ))

        records = cursor.fetchall()

        conn.close()

        # Header
        header = ctk.CTkFrame(
            self.log
        )

        header.pack(
            fill="x",
            pady=(0, 5)
        )

        headers = [
            "Employee ID",
            "Name",
            "Department",
            "Date",
            "Clock In",
            "Clock Out",
            "Hours"
        ]

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

        # Records
        for record in records:

            (
                employee_id,
                name,
                department,
                date,
                clock_in,
                clock_out,
                hours
            ) = record

            row = ctk.CTkFrame(
                self.log
            )

            row.pack(
                fill="x",
                pady=2
            )

            values = [
                employee_id,
                name,
                department,
                date,
                self.format_time(clock_in),
                self.format_time(clock_out),
                (
                    f"{hours:.2f}"
                    if hours is not None
                    else "--"
                )
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
    # FORMAT TIME
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
