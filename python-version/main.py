import customtkinter as ctk

import database
import dashboard
import employees
import attendance
import reports


class AttendanceSystem:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Employee Attendance System")
        self.root.geometry("1100x700")
        self.root.minsize(950, 600)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Create the database
        database.create_tables()

        self.create_layout()
        self.show_dashboard()

    def create_layout(self):
        # Main container
        self.main_frame = ctk.CTkFrame(
            self.root,
            corner_radius=0,
            fg_color="#f5f5f5"
        )
        self.main_frame.pack(fill="both", expand=True)

        # Sidebar
        self.sidebar = ctk.CTkFrame(
            self.main_frame,
            width=220,
            corner_radius=0,
            fg_color="#1f1f1f"
        )
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Title
        self.title_label = ctk.CTkLabel(
            self.sidebar,
            text="ATTENDANCE\nSYSTEM",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="white"
        )
        self.title_label.pack(
            padx=20,
            pady=(35, 40)
        )

        # Navigation buttons
        self.dashboard_button = ctk.CTkButton(
            self.sidebar,
            text="Dashboard",
            height=45,
            corner_radius=8,
            command=self.show_dashboard
        )
        self.dashboard_button.pack(
            padx=20,
            pady=5,
            fill="x"
        )

        self.attendance_button = ctk.CTkButton(
            self.sidebar,
            text="Attendance",
            height=45,
            corner_radius=8,
            command=self.show_attendance
        )
        self.attendance_button.pack(
            padx=20,
            pady=5,
            fill="x"
        )

        self.employees_button = ctk.CTkButton(
            self.sidebar,
            text="Employees",
            height=45,
            corner_radius=8,
            command=self.show_employees
        )
        self.employees_button.pack(
            padx=20,
            pady=5,
            fill="x"
        )

        self.reports_button = ctk.CTkButton(
            self.sidebar,
            text="Reports",
            height=45,
            corner_radius=8,
            command=self.show_reports
        )
        self.reports_button.pack(
            padx=20,
            pady=5,
            fill="x"
        )

        # Exit button
        self.exit_button = ctk.CTkButton(
            self.sidebar,
            text="Exit",
            height=45,
            corner_radius=8,
            fg_color="#444444",
            hover_color="#333333",
            command=self.exit_application
        )
        self.exit_button.pack(
            side="bottom",
            padx=20,
            pady=25,
            fill="x"
        )

        # Content area
        self.content_frame = ctk.CTkFrame(
            self.main_frame,
            corner_radius=0,
            fg_color="#f5f5f5"
        )
        self.content_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_content()

        dashboard.show_dashboard(
            self.content_frame
        )

    def show_attendance(self):
        self.clear_content()

        attendance.show_attendance(
            self.content_frame
        )

    def show_employees(self):
        self.clear_content()

        employees.show_employees(
            self.content_frame
        )

    def show_reports(self):
        self.clear_content()

        reports.show_reports(
            self.content_frame
        )

    def exit_application(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = AttendanceSystem()
    app.run()
