import customtkinter as ctk
from datetime import datetime

from database import connect_db


class DashboardPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(
            (0, 1, 2, 3),
            weight=1
        )

        self.create_dashboard()

    # =====================================================
    # DASHBOARD
    # =====================================================

    def create_dashboard(self):

        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 30, "bold")
        )

        title.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky="w",
            pady=(10, 5)
        )

        today = datetime.now().strftime(
            "%A, %B %d, %Y"
        )

        date_label = ctk.CTkLabel(
            self,
            text=today,
            font=("Arial", 15)
        )

        date_label.grid(
            row=1,
            column=0,
            columnspan=4,
            sticky="w",
            pady=(0, 25)
        )

        # Get statistics
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM employees"
        )

        total_employees = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*)
            FROM attendance
            WHERE date = ?
            AND clock_out IS NULL
        """, (
            datetime.now().strftime("%Y-%m-%d"),
        ))

        clocked_in = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*)
            FROM attendance
            WHERE date = ?
            AND clock_out IS NOT NULL
        """, (
            datetime.now().strftime("%Y-%m-%d"),
        ))

        clocked_out = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*)
            FROM attendance
            WHERE date = ?
        """, (
            datetime.now().strftime("%Y-%m-%d"),
        ))

        today_attendance = cursor.fetchone()[0]

        conn.close()

        # Cards
        self.create_card(
            "Total Employees",
            total_employees,
            2,
            0
        )

        self.create_card(
            "Clocked In",
            clocked_in,
            2,
            1
        )

        self.create_card(
            "Clocked Out",
            clocked_out,
            2,
            2
        )

        self.create_card(
            "Today's Records",
            today_attendance,
            2,
            3
        )

        # Current employees
        current_title = ctk.CTkLabel(
            self,
            text="Employees Currently Working",
            font=("Arial", 22, "bold")
        )

        current_title.grid(
            row=3,
            column=0,
            columnspan=4,
            sticky="w",
            pady=(40, 15)
        )

        self.current_frame = ctk.CTkScrollableFrame(
            self
        )

        self.current_frame.grid(
            row=4,
            column=0,
            columnspan=4,
            sticky="nsew"
        )

        self.grid_rowconfigure(
            4,
            weight=1
        )

        self.load_current_employees()

    # =====================================================
    # CARD
    # =====================================================

    def create_card(
        self,
        title,
        value,
        row,
        column
    ):

        card = ctk.CTkFrame(
            self,
            height=130
        )

        card.grid(
            row=row,
            column=column,
            sticky="nsew",
            padx=5
        )

        card.grid_propagate(False)

        label = ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 14)
        )

        label.pack(
            pady=(25, 5)
        )

        number = ctk.CTkLabel(
            card,
            text=str(value),
            font=("Arial", 30, "bold")
        )

        number.pack()

    # =====================================================
    # CURRENT EMPLOYEES
    # =====================================================

    def load_current_employees(self):

        for widget in self.current_frame.winfo_children():
            widget.destroy()

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                employees.employee_id,
                employees.name,
                employees.department,
                attendance.clock_in
            FROM attendance

            JOIN employees
            ON attendance.employee_id =
               employees.employee_id

            WHERE attendance.date = ?
            AND attendance.clock_out IS NULL

            ORDER BY attendance.clock_in
        """, (
            datetime.now().strftime("%Y-%m-%d"),
        ))

        employees = cursor.fetchall()

        conn.close()

        if not employees:

            label = ctk.CTkLabel(
                self.current_frame,
                text="No employees are currently clocked in.",
                font=("Arial", 15)
            )

            label.pack(
                pady=30
            )

            return

        for employee in employees:

            employee_id = employee[0]
            name = employee[1]
            department = employee[2]
            clock_in = employee[3]

            row = ctk.CTkFrame(
                self.current_frame
            )

            row.pack(
                fill="x",
                pady=5
            )

            text = (
                f"{employee_id}    "
                f"{name}    "
                f"{department}    "
                f"Clock In: {clock_in}"
            )

            label = ctk.CTkLabel(
                row,
                text=text,
                font=("Arial", 13),
                anchor="w"
            )

            label.pack(
                padx=15,
                pady=12,
                anchor="w"
            )
