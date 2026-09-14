import customtkinter as ctk
from tkinter import messagebox

import database
from dashboard import DashboardPage
from employees import EmployeesPage
from attendance import AttendancePage


class AttendanceApplication:

    def __init__(self, root):

        self.root = root

        # ====================================================
        # DATABASE
        # ====================================================

        database.create_tables()

        # ====================================================
        # WINDOW SETTINGS
        # ====================================================

        self.root.title(
            "Company Attendance System"
        )

        self.root.geometry(
            "1250x780"
        )

        self.root.minsize(
            1050,
            680
        )

        # ====================================================
        # APPEARANCE
        # ====================================================

        ctk.set_appearance_mode(
            "light"
        )

        ctk.set_default_color_theme(
            "blue"
        )

        # ====================================================
        # COLORS
        # ====================================================

        self.background = "#F5F5F7"
        self.sidebar_color = "#FFFFFF"
        self.text_color = "#1D1D1F"
        self.secondary_text = "#6E6E73"

        self.blue = "#0071E3"
        self.hover_blue = "#E8F2FC"

        self.border = "#E5E5E7"

        # ====================================================
        # CURRENT PAGE
        # ====================================================

        self.current_page = None

        self.current_button = None

        # ====================================================
        # BUILD APPLICATION
        # ====================================================

        self.create_layout()

        self.create_sidebar()

        self.create_content()

        # ====================================================
        # OPEN DASHBOARD
        # ====================================================

        self.show_dashboard()

    # ========================================================
    # MAIN LAYOUT
    # ========================================================

    def create_layout(self):

        self.main_frame = ctk.CTkFrame(
            self.root,
            fg_color=self.background,
            corner_radius=0
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

    # ========================================================
    # SIDEBAR
    # ========================================================

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self.main_frame,
            width=240,
            fg_color=self.sidebar_color,
            corner_radius=0,
            border_width=1,
            border_color=self.border
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(
            False
        )

        # ----------------------------------------------------
        # BRAND
        # ----------------------------------------------------

        brand_frame = ctk.CTkFrame(
            self.sidebar,
            fg_color="transparent"
        )

        brand_frame.pack(
            fill="x",
            padx=20,
            pady=(25, 30)
        )

        # Logo
        logo = ctk.CTkLabel(
            brand_frame,
            text="A",
            width=42,
            height=42,
            corner_radius=12,
            fg_color=self.blue,
            text_color="white",
            font=ctk.CTkFont(
                size=20,
                weight="bold"
            )
        )

        logo.pack(
            side="left"
        )

        # Brand text
        brand_text = ctk.CTkFrame(
            brand_frame,
            fg_color="transparent"
        )

        brand_text.pack(
            side="left",
            padx=10
        )

        company_label = ctk.CTkLabel(
            brand_text,
            text="Attendance",
            font=ctk.CTkFont(
                size=15,
                weight="bold"
            ),
            text_color=self.text_color
        )

        company_label.pack(
            anchor="w"
        )

        version_label = ctk.CTkLabel(
            brand_text,
            text="Management System",
            font=ctk.CTkFont(
                size=10
            ),
            text_color=self.secondary_text
        )

        version_label.pack(
            anchor="w"
        )

        # ----------------------------------------------------
        # NAVIGATION LABEL
        # ----------------------------------------------------

        navigation_label = ctk.CTkLabel(
            self.sidebar,
            text="MAIN MENU",
            font=ctk.CTkFont(
                size=10,
                weight="bold"
            ),
            text_color=self.secondary_text
        )

        navigation_label.pack(
            anchor="w",
            padx=25,
            pady=(0, 10)
        )

        # ----------------------------------------------------
        # NAVIGATION BUTTONS
        # ----------------------------------------------------

        self.dashboard_button = self.create_nav_button(
            "Dashboard",
            self.show_dashboard
        )

        self.employees_button = self.create_nav_button(
            "Employees",
            self.show_employees
        )

        self.attendance_button = self.create_nav_button(
            "Attendance",
            self.show_attendance
        )

        # ----------------------------------------------------
        # SPACER
        # ----------------------------------------------------

        spacer = ctk.CTkFrame(
            self.sidebar,
            fg_color="transparent"
        )

        spacer.pack(
            fill="both",
            expand=True
        )

        # ----------------------------------------------------
        # SYSTEM INFO
        # ----------------------------------------------------

        info_frame = ctk.CTkFrame(
            self.sidebar,
            fg_color="#F5F5F7",
            corner_radius=12
        )

        info_frame.pack(
            fill="x",
            padx=15,
            pady=(0, 15)
        )

        system_title = ctk.CTkLabel(
            info_frame,
            text="Attendance System",
            font=ctk.CTkFont(
                size=11,
                weight="bold"
            ),
            text_color=self.text_color
        )

        system_title.pack(
            anchor="w",
            padx=12,
            pady=(12, 2)
        )

        system_description = ctk.CTkLabel(
            info_frame,
            text="Employee time tracking",
            font=ctk.CTkFont(
                size=10
            ),
            text_color=self.secondary_text
        )

        system_description.pack(
            anchor="w",
            padx=12,
            pady=(0, 12)
        )

        # ----------------------------------------------------
        # EXIT BUTTON
        # ----------------------------------------------------

        exit_button = ctk.CTkButton(
            self.sidebar,
            text="Exit Application",
            height=40,
            corner_radius=8,
            fg_color="#F5F5F7",
            hover_color="#E5E5E7",
            text_color=self.text_color,
            font=ctk.CTkFont(
                size=12,
                weight="bold"
            ),
            command=self.exit_application
        )

        exit_button.pack(
            fill="x",
            padx=15,
            pady=(0, 20)
        )

    # ========================================================
    # CREATE NAVIGATION BUTTON
    # ========================================================

    def create_nav_button(
        self,
        text,
        command
    ):

        button = ctk.CTkButton(
            self.sidebar,
            text=text,
            height=45,
            corner_radius=9,
            fg_color="transparent",
            hover_color=self.hover_blue,
            text_color=self.text_color,
            anchor="w",
            font=ctk.CTkFont(
                size=13
            ),
            command=command
        )

        button.pack(
            fill="x",
            padx=15,
            pady=3
        )

        return button

    # ========================================================
    # CONTENT AREA
    # ========================================================

    def create_content(self):

        self.content = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.background,
            corner_radius=0
        )

        self.content.pack(
            side="left",
            fill="both",
            expand=True
        )

    # ========================================================
    # CLEAR CONTENT
    # ========================================================

    def clear_content(self):

        for widget in self.content.winfo_children():

            widget.destroy()

    # ========================================================
    # ACTIVE NAVIGATION BUTTON
    # ========================================================

    def set_active_button(
        self,
        button
    ):

        buttons = [
            self.dashboard_button,
            self.employees_button,
            self.attendance_button
        ]

        for nav_button in buttons:

            nav_button.configure(
                fg_color="transparent",
                text_color=self.text_color
            )

        button.configure(
            fg_color=self.hover_blue,
            text_color=self.blue
        )

        self.current_button = button

    # ========================================================
    # DASHBOARD
    # ========================================================

    def show_dashboard(self):

        self.clear_content()

        self.set_active_button(
            self.dashboard_button
        )

        self.current_page = DashboardPage(
            self.content
        )

    # ========================================================
    # EMPLOYEES
    # ========================================================

    def show_employees(self):

        self.clear_content()

        self.set_active_button(
            self.employees_button
        )

        self.current_page = EmployeesPage(
            self.content
        )

    # ========================================================
    # ATTENDANCE
    # ========================================================

    def show_attendance(self):

        self.clear_content()

        self.set_active_button(
            self.attendance_button
        )

        self.current_page = AttendancePage(
            self.content
        )

    # ========================================================
    # EXIT APPLICATION
    # ========================================================

    def exit_application(self):

        answer = messagebox.askyesno(
            "Exit Application",
            "Are you sure you want to exit?"
        )

        if answer:

            self.root.destroy()


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    root = ctk.CTk()

    application = AttendanceApplication(
        root
    )

    root.mainloop()
