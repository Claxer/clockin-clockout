# Company Attendance System – Python

A Python-based **Employee Attendance Management System** designed to help companies manage employees and track their daily attendance. The system provides a desktop graphical user interface where employees can be registered, clock in and clock out, and have their attendance records stored automatically.

The project was developed as a practical Python application demonstrating **GUI development, SQLite database management, CRUD operations, date and time handling, application navigation, and modular programming**.

---

## Description

The **Company Attendance System** is a desktop attendance management application built with Python and CustomTkinter.

The system allows a company or organization to maintain employee records and monitor their attendance through a centralized application.

Employees can:

* Clock in when they start their workday
* Clock out when they finish their workday
* View their attendance information
* Have their attendance automatically recorded with the current date and time

Administrators or authorized users can:

* Add employees
* View employee records
* Manage employee information
* Monitor attendance records
* Review clock-in and clock-out information

All important information is stored locally using an **SQLite database**, allowing the data to remain available even after the application is closed.

---

# Features

## Dashboard

The dashboard provides a central overview of the attendance system.

Features include:

* Attendance system overview
* Quick access to different sections
* Navigation between application pages
* Employee-related information
* Attendance-related information
* Organized desktop interface

The dashboard acts as the main control center of the application.

---

## Employee Management

The Employee Management section allows users to maintain employee information.

Features include:

* Add new employees
* View registered employees
* Manage employee records
* Store employee information in the database
* Select employees for attendance actions
* Organize employee data

Employee information is connected to attendance records so that attendance can be associated with the correct employee.

---

## Clock In

The Clock In feature records when an employee begins their work session.

When an employee clocks in, the system:

1. Identifies the selected employee.
2. Gets the current date and time.
3. Creates an attendance record.
4. Stores the clock-in information in SQLite.
5. Associates the attendance record with the employee.

The system helps prevent unnecessary duplicate clock-in records for the same work session.

Example:

```text
Employee: Jose Navoa
Date: September 3, 2026
Clock In: 08:02 AM
Status: Currently Working
```

---

## Clock Out

The Clock Out feature records when an employee finishes their work session.

When an employee clocks out, the system:

1. Identifies the employee.
2. Finds the employee's active attendance record.
3. Gets the current date and time.
4. Updates the attendance record.
5. Saves the clock-out time.

Example:

```text
Employee: Jose Navoa
Date: September 3, 2026
Clock In: 08:02 AM
Clock Out: 05:04 PM
Status: Completed
```

This allows the system to maintain a complete record of an employee's working session.

---

## Attendance Records

The Attendance section allows users to monitor previously recorded attendance information.

Attendance records can contain:

* Employee ID
* Employee name
* Attendance date
* Clock-in time
* Clock-out time
* Attendance session information

Example:

| Employee   | Date       | Clock In | Clock Out |
| ---------- | ---------- | -------- | --------- |
| Jose Navoa | 2026-09-03 | 08:02 AM | 05:04 PM  |
| Employee 2 | 2026-09-03 | 08:15 AM | 05:10 PM  |

The attendance records are stored in the database so they remain available between application sessions.

---

# Attendance Workflow

The basic workflow of the application is:

```text
Launch Application
       │
       ▼
    Dashboard
       │
       ▼
Employee Management
       │
       ▼
 Select Employee
       │
       ▼
   ┌───────────────┐
   │               │
   ▼               ▼
Clock In        Clock Out
   │               │
   ▼               ▼
Record Start    Record End
   │               │
   └───────┬───────┘
           ▼
   Attendance Database
```

---

# Application Structure

The project uses a modular structure where different Python files are responsible for different parts of the application.

```text
clockin-clockout/
│
├── python-version/
│   │
│   ├── main.py
│   ├── database.py
│   ├── dashboard.py
│   ├── employees.py
│   ├── attendance.py
│   └── company_attendance.db
│
├── LICENSE
└── README.md
```

### `main.py`

The main entry point of the application.

Responsible for:

* Starting the application
* Initializing the GUI
* Loading the required pages
* Starting the main application window

---

### `database.py`

Handles the SQLite database.

Responsible for:

* Creating the database
* Creating database tables
* Connecting to SQLite
* Storing employee information
* Storing attendance information
* Managing database operations

Keeping database operations in a separate file makes the application easier to maintain.

---

### `dashboard.py`

Contains the main dashboard interface.

Responsible for:

* Displaying the main application layout
* Navigation
* Dashboard information
* Connecting different sections of the system

---

### `employees.py`

Handles employee management functionality.

Responsible for:

* Adding employees
* Displaying employee information
* Managing employee records
* Selecting employees for attendance actions

---

### `attendance.py`

Handles attendance-related functionality.

Responsible for:

* Clocking employees in
* Clocking employees out
* Recording attendance dates
* Recording clock-in times
* Recording clock-out times
* Displaying attendance information

---

### `company_attendance.db`

The SQLite database used by the application.

It stores persistent application data such as employee and attendance information.

> The database file may be created automatically when the application is first launched.

---

# Database

The system uses **SQLite** as its database engine.

SQLite was selected because it is lightweight and does not require a separate database server.

The database can store information such as:

### Employee Information

* Employee ID
* Employee name
* Employee details

### Attendance Information

* Attendance ID
* Employee ID
* Attendance date
* Clock-in time
* Clock-out time

A simplified relationship can be represented as:

```text
Employees
    │
    │ Employee ID
    ▼
Attendance Records
    │
    ├── Date
    ├── Clock In
    └── Clock Out
```

This allows multiple attendance records to be associated with an employee.

---

# Data Persistence

One of the main advantages of using SQLite is that attendance information is not lost when the application closes.

For example:

```text
Application Open
      ↓
Employee clocks in
      ↓
Attendance saved
      ↓
Application closes
      ↓
Application opens again
      ↓
Previous attendance remains available
```

This makes the system more practical than storing attendance only in temporary Python variables.

---

# User Interface

The application uses **CustomTkinter** to provide a modernized desktop interface compared with standard Tkinter widgets.

The interface is organized into different sections so users can easily navigate between:

* Dashboard
* Employees
* Attendance
* Clock In
* Clock Out

The design focuses on keeping the attendance workflow simple and easy to understand.

---

# Technologies Used

### Programming Language

**Python**

Used as the main programming language for the entire application.

### GUI Framework

**CustomTkinter**

Used to create the desktop graphical user interface.

### Database

**SQLite**

Used for local and persistent data storage.

### Date and Time

**datetime**

Used to automatically obtain and record:

* Current date
* Current time
* Clock-in time
* Clock-out time

---

# Python Concepts Demonstrated

This project demonstrates several important Python programming concepts.

## Variables and Data Types

Used to store employee information, attendance data, dates, times, and application states.

## Functions

Used to organize specific operations such as:

* Adding employees
* Clocking in
* Clocking out
* Retrieving attendance
* Database operations

## Classes and Object-Oriented Programming

The application uses classes to organize GUI pages and application components.

## Modules

The project is separated into multiple Python files to keep the code organized.

## Exception Handling

Error handling can be used to prevent the application from crashing when unexpected input or database problems occur.

## CRUD Operations

The application demonstrates database operations such as:

* **Create** – Add employee and attendance records
* **Read** – Display employee and attendance information
* **Update** – Update attendance records when an employee clocks out
* **Delete** – Manage or remove records where supported

## Database Queries

SQL commands are used to interact with the SQLite database.

---

# How It Works

### Step 1 – Launch

Start the application using Python.

### Step 2 – Open the Dashboard

The dashboard provides access to the different system functions.

### Step 3 – Manage Employees

Add or view employees using the Employee Management section.

### Step 4 – Select an Employee

Choose the employee who needs to record attendance.

### Step 5 – Clock In

The system records the employee's current date and time.

### Step 6 – Employee Works

The attendance record remains active while the employee is working.

### Step 7 – Clock Out

When the employee finishes work, the system records the current time as the clock-out time.

### Step 8 – View Attendance

The completed attendance record can be viewed through the Attendance section.

---

# Example Attendance Session

Suppose an employee starts work at 8:00 AM.

```text
Employee
   ↓
Jose Navoa
   ↓
Clock In
   ↓
08:00 AM
   ↓
Work Session
   ↓
Clock Out
   ↓
05:00 PM
```

The database can then contain:

```text
Employee: Jose Navoa
Date: 2026-09-03
Clock In: 08:00 AM
Clock Out: 05:00 PM
```

---

# Validation and Attendance Control

The application is designed to prevent common attendance problems.

Examples include:

* Preventing unnecessary duplicate clock-ins
* Preventing clock-out without an active attendance session
* Associating attendance with the correct employee
* Automatically recording the current date
* Automatically recording the current time
* Maintaining attendance records in the database

These controls help keep attendance information consistent.

---

# Installation

## Requirements

Before running the application, make sure Python is installed on your computer.

You can check your Python installation using:

```bash
python --version
```

If Python is installed correctly, the command should display your installed Python version.

---

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/company-attendance-system.git
```

---

## 2. Open the Project

Navigate to the project folder:

```bash
cd company-attendance-system
```

Then enter the Python version:

```bash
cd python-version
```

---

## 3. Install CustomTkinter

Install the required GUI library:

```bash
pip install customtkinter
```

If your system uses `pip3`, you can use:

```bash
pip3 install customtkinter
```

---

## 4. Run the Application

Run:

```bash
python main.py
```

The Company Attendance System should then open as a desktop application.

---

# Running in Visual Studio Code

The project can also be run directly through **Visual Studio Code**.

### Step 1

Open Visual Studio Code.

### Step 2

Select:

```text
File → Open Folder
```

Choose the project folder.

### Step 3

Open the terminal:

```text
Terminal → New Terminal
```

### Step 4

Navigate to the Python version:

```bash
cd python-version
```

### Step 5

Run:

```bash
python main.py
```

---

# Troubleshooting

## Python is not recognized

If Windows displays:

```text
Python was not found
```

Python may not be installed or may not have been added to the system PATH.

Check the installation using:

```bash
py --version
```

If `py` works, you can run the application using:

```bash
py main.py
```

---

## CustomTkinter is not installed

If you receive:

```text
ModuleNotFoundError: No module named 'customtkinter'
```

Install CustomTkinter:

```bash
pip install customtkinter
```

Then run:

```bash
python main.py
```

---

## Database does not exist

The SQLite database can be created by the application when the database initialization code runs.

If the database is missing, make sure the application is being started from the correct project directory.

---

# Project Goals

The main goals of this project are to create a functional attendance system while practicing Python programming and software development concepts.

The project focuses on:

* Employee management
* Attendance tracking
* Clock-in and clock-out functionality
* Database management
* GUI development
* Data persistence
* Modular programming
* User interaction

---

# Future Improvements

The current application can be expanded with additional features.

Possible improvements include:

### Attendance Features

* Automatic working-hours calculation
* Late arrival detection
* Early departure detection
* Overtime calculation
* Attendance status
* Daily attendance summaries
* Weekly attendance summaries
* Monthly attendance summaries
* Absence tracking

### Employee Features

* Employee profile pictures
* Employee departments
* Job positions
* Contact information
* Employee search
* Employee filtering
* Employee status

### Reports

* Export attendance to CSV
* Export attendance to Excel
* Generate PDF reports
* Monthly attendance reports
* Individual employee reports
* Payroll-ready attendance reports

### Authentication

* Admin login
* Employee login
* Role-based permissions
* Password protection
* Account management

### Interface

* Improved animations
* Page transition animations
* Notifications
* Confirmation dialogs
* Improved dashboard statistics
* More responsive layouts
* Dark and light themes

### Advanced Features

* Web-based version
* Cloud database
* Remote attendance tracking
* Multi-user support
* API integration
* Automatic backups
* Email notifications
* QR code attendance
* Biometric attendance integration

---

# Planned Web Version

A web-based version of the Company Attendance System can also be developed using:

```text
HTML
CSS
JavaScript
```

The web version can provide similar functionality to the Python desktop application while allowing the system to be accessed through a browser.

A possible future structure would be:

```text
company-attendance-system/
│
├── python-version/
│   ├── main.py
│   ├── database.py
│   ├── dashboard.py
│   ├── employees.py
│   └── attendance.py
│
├── web-version/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── LICENSE
└── README.md
```

This allows the Python and Web versions to exist within the same project while keeping their source code separated.

---

# Learning Outcomes

Through this project, the following programming and development skills are practiced:

* Python programming
* Object-oriented programming
* GUI development
* SQLite database management
* SQL queries
* CRUD operations
* Event-driven programming
* Date and time manipulation
* Input validation
* Error handling
* Modular application design
* File organization
* User interface design
* Basic software architecture
* Git and GitHub project management

---

# Project Status

**Current Status:** Functional Python Desktop Application

The Python version provides the core functionality required for an employee attendance system, including employee management, clock-in, clock-out, and attendance record storage.

Future versions may expand the project with more advanced attendance calculations, reporting, authentication, and web functionality.

---

# Purpose

This project was created as an educational and practical Python application.

It demonstrates how multiple programming concepts can be combined to create a functional desktop application rather than a collection of individual programming exercises.

The project combines:

```text
Python
   +
CustomTkinter
   +
SQLite
   +
Date & Time
   +
CRUD Operations
   +
Object-Oriented Programming
   ↓
Company Attendance System
```

---

# Author

**Jose Navoa**

Information Technology Student

---

# License

This project is intended for **educational and personal use**.

See the `LICENSE` file included in the repository for additional information.
