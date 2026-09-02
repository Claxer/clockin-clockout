# Company Attendance System – Python

A Python-based **Employee Attendance Management System** designed to record and manage employee clock-in and clock-out activities. The application provides a simple desktop interface for managing employees and tracking their attendance records.

## Description

The Company Attendance System allows employees to record their working hours by clocking in when they start work and clocking out when they finish.

The application automatically records the date and time of each attendance action and stores the information in an SQLite database. It also provides separate sections for viewing employees, monitoring attendance, and managing attendance-related information.

## Features

### Dashboard

* Overview of the attendance system
* Quick access to employee and attendance sections
* Displays important attendance information

### Employee Management

* Add employees
* View employee information
* Manage employee records
* Organize employee data

### Clock In / Clock Out

* Record employee clock-in time
* Record employee clock-out time
* Automatically records the current date and time
* Prevents unnecessary duplicate attendance records
* Tracks employee working sessions

### Attendance Records

* View attendance history
* Track clock-in and clock-out times
* Monitor employee attendance
* Store attendance information in the database

### Database

* Uses SQLite for local data storage
* Stores employee information
* Stores attendance records
* Keeps data available between application sessions

## Technologies Used

* **Python** – Main programming language
* **CustomTkinter** – Graphical User Interface
* **SQLite** – Database management
* **Datetime** – Date and time handling

## Project Structure

```text
clockin-clockout/
│
├── python-version/
│   ├── attendance.py
│   ├── company_attendance.db
│   ├── dashboard.py
│   ├── database.py
│   ├── employees.py
│   └── main.py
│
├── LICENSE
└── README.md
```

> The exact file structure may vary depending on the current version of the project.

## How It Works

1. Launch the application.
2. Open the **Employees** section to manage employee information.
3. Select an employee for an attendance action.
4. Use **Clock In** when the employee starts working.
5. Use **Clock Out** when the employee finishes working.
6. The system records the date and time automatically.
7. Attendance information can be viewed through the **Attendance** section.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/company-attendance-system.git
```

### 2. Open the Project

```bash
cd company-attendance-system
```

### 3. Install Dependencies

If CustomTkinter is not installed:

```bash
pip install customtkinter
```

### 4. Run the Application

```bash
python main.py
```

## Database

The application uses **SQLite**, so no separate database server is required.

The database stores information such as:

* Employee ID
* Employee name
* Employee information
* Attendance date
* Clock-in time
* Clock-out time

The database can be automatically created when the application starts if it does not already exist.

## Future Improvements

Possible future improvements include:

* Employee search and filtering
* Attendance reports
* Export attendance records to CSV or Excel
* Monthly attendance summaries
* Total working-hours calculation
* Late and early detection
* Admin login system
* Employee profile pictures
* Dark and light themes
* Web-based version
* Cloud database integration

## Purpose

This project was created as a practical Python application to demonstrate the use of:

* GUI development
* Database management
* Object-oriented programming
* Date and time handling
* CRUD operations
* Application structure
* User interaction

## Author

**Jose Navoa**

Information Technology Student

## License

This project is intended for educational and personal use.
