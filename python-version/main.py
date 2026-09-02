import customtkinter as ctk

from database import create_database
from dashboard import DashboardPage
from employees import EmployeesPage
from attendance import AttendancePage


class CompanyAttendance(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Company Attendance System")
        self.geometry("1200x750")
        self.minsize(1000, 650)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()

        self.show_dashboard()

    # =====================================================
    # SIDEBAR
    # =====================================================

    def create_sidebar(self):

        sidebar = ctk.CTkFrame(
            self,
            width=230,
            corner_radius=0
        )

        sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        sidebar.grid_propagate(False)

        # Company title
        title = ctk.CTkLabel(
            sidebar,
            text="COMPANY\nATTENDANCE",
            font=("Arial", 22, "bold")
        )

        title.pack(
            pady=(40, 40)
        )

        # Dashboard
        ctk.CTkButton(
            sidebar,
            text="Dashboard",
            height=45,
            command=self.show_dashboard
        ).pack(
            fill="x",
            padx=20,
            pady=5
        )

        # Employees
        ctk.CTkButton(
            sidebar,
            text="Employees",
            height=45,
            command=self.show_employees
        ).pack(
            fill="x",
            padx=20,
            pady=5
        )

        # Attendance
        ctk.CTkButton(
            sidebar,
            text="Attendance",
            height=45,
            command=self.show_attendance
        ).pack(
            fill="x",
            padx=20,
            pady=5
        )

        # Exit
        ctk.CTkButton(
            sidebar,
            text="Exit",
            height=45,
            fg_color="#8B0000",
            hover_color="#A00000",
            command=self.destroy
        ).pack(
            side="bottom",
            fill="x",
            padx=20,
            pady=30
        )

    # =====================================================
    # CLEAR CONTENT
    # =====================================================

    def clear_content(self):

        for widget in self.winfo_children():

            if widget.grid_info().get("column") == 1:
                widget.destroy()

    # =====================================================
    # DASHBOARD
    # =====================================================

    def show_dashboard(self):

        self.clear_content()

        page = DashboardPage(self)

        page.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=20,
            pady=20
        )

    # =====================================================
    # EMPLOYEES
    # =====================================================

    def show_employees(self):

        self.clear_content()

        page = EmployeesPage(self)

        page.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=20,
            pady=20
        )

    # =====================================================
    # ATTENDANCE
    # =====================================================

    def show_attendance(self):

        self.clear_content()

        page = AttendancePage(self)

        page.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=20,
            pady=20
        )


# =========================================================
# START
# =========================================================

if __name__ == "__main__":

    create_database()

    app = CompanyAttendance()

    app.mainloop()
