# Company Attendance System

A complete **Employee Attendance Management System** developed with two versions: a **Python Desktop Application** and a **Web Application**.

The system is designed to help companies manage employee information, record daily attendance, track Clock In and Clock Out activity, and generate attendance reports.

The project demonstrates how the same attendance-management concept can be implemented across different platforms while using appropriate technologies for each version.

---

# Overview

The **Company Attendance System** provides a centralized way to manage employees and record their attendance.

The project currently contains two available versions:

| Version        | Technologies                  | Platform    |
| -------------- | ----------------------------- | ----------- |
| Python Version | Python, CustomTkinter, SQLite | Desktop     |
| Web Version    | HTML, CSS, JavaScript         | Web Browser |

The Python version is organized into separate modules for the dashboard, employee management, attendance tracking, database operations, and reports.

Both versions are designed around the same core attendance workflow:

```text
Employee
   ↓
Employee Management
   ↓
Select Employee
   ↓
Clock In
   ↓
Work Session
   ↓
Clock Out
   ↓
Attendance Record
   ↓
Attendance Reports
```

---

# Features

## Dashboard

The Dashboard serves as the main control center of the Python attendance system.

It provides access to the major sections of the application:

* Dashboard
* Attendance
* Employees
* Reports
* Exit

The dashboard provides a quick overview of employee attendance.

The Python dashboard includes:

* Total Employees
* Present Today
* Late Today
* Absent Today
* Today's attendance records
* Recent attendance records
* Current date
* Attendance status information

Example:

```text
Total Employees    10
Present Today       7
Late Today          3
Absent Today        3
```

The dashboard also displays recent attendance records containing information such as:

```text
Employee
Date
Time In
Time Out
Status
```

---

# Employee Management

The Employee Management section allows users to maintain employee information.

Features include:

* Add employees
* View employees
* Search employees
* Edit employee information
* Delete employees
* Refresh employee list
* Select employees for attendance
* Employee ID management
* Full name management
* Department management
* Position management
* Contact number management

Each employee can contain:

```text
Employee ID
Full Name
Position
Department
Contact Number
```

Example:

```text
Employee ID: 1
Full Name: Jose Navoa
Department: IT
Position: IT Assistant
Contact: 09123456789
```

Employee information is connected to attendance records so that each attendance record can be associated with the correct employee.

---

# Add Employee

The system provides a dedicated form for adding new employees.

The user can enter:

```text
Full Name
Position
Department
Contact Number
```

Example:

```text
Full Name: Jose Navoa
Position: IT Assistant
Department: IT
Contact Number: 09123456789

[ Save Employee ]
```

The employee is saved into the SQLite database after successful registration.

The system also checks that the employee name is provided before saving the record.

---

# Employee Search

The Python desktop version includes an employee search function.

Users can search employee records using:

```text
Employee Name
Position
Department
```

Example:

```text
Search: Jose

1 | Jose Navoa | IT Assistant | IT | 09123456789
```

The employee list can also be refreshed to display all available employee records.

---

# Edit Employee

The Employee Management section allows existing employee information to be edited.

Users can update:

```text
Full Name
Position
Department
Contact Number
```

After saving the changes, the employee list is refreshed automatically.

Example workflow:

```text
Select Employee
      ↓
Edit
      ↓
Modify Information
      ↓
Save Changes
      ↓
Employee Record Updated
```

---

# Delete Employee

The Employee Management section includes a delete function.

Users can select an employee and remove the employee from the database.

Before deletion, the system displays a confirmation message:

```text
Are you sure you want to delete this employee?
```

This helps prevent accidental deletion.

---

# Clock In

The Clock In feature records the beginning of an employee's work session.

When an employee clocks in, the system:

1. Identifies the selected employee.
2. Checks whether an employee was selected.
3. Checks whether the employee already has an attendance record for the day.
4. Gets the current date.
5. Gets the current time.
6. Determines the attendance status.
7. Creates an attendance record.
8. Saves the record to SQLite.
9. Refreshes the attendance information.

Example:

```text
Employee: Jose Navoa
Date: October 7, 2026
Clock In: 08:02:15
Status: Late
```

The current Python version considers an employee **Late** when the employee clocks in after **8:00 AM**.

Employees who clock in at or before 8:00 AM are marked:

```text
Present
```

The system prevents an employee from creating another attendance record when the employee already has an attendance record for the current day.

---

# Clock Out

The Clock Out feature records when an employee finishes their work session.

When an employee clocks out, the system:

1. Identifies the selected employee.
2. Checks whether an employee was selected.
3. Searches for the employee's attendance record for the current day.
4. Checks whether the employee has already clocked out.
5. Gets the current time.
6. Updates the attendance record.
7. Saves the clock-out information.
8. Refreshes the attendance page.

Example:

```text
Employee: Jose Navoa
Date: October 7, 2026
Clock In: 08:02:15
Clock Out: 17:03:21
Status: Late
```

The system prevents an employee from clocking out if there is no attendance record for the current day.

It also prevents an employee from clocking out more than once for the same attendance record.

---

# Attendance Page

The Attendance page is the main area for recording and viewing daily employee attendance.

It includes:

* Employee selection
* Clock In
* Clock Out
* Today's attendance
* Attendance records
* Employee name
* Date
* Time In
* Time Out
* Attendance status
* Refresh functionality

The employee can be selected using a dropdown menu.

Example:

```text
Employee:
[ 1 - Jose Navoa ]

[ Clock In ] [ Clock Out ]
```

---

# Today's Attendance

The Attendance page automatically displays attendance records for the current date.

The table displays:

```text
ID
Employee
Date
Time In
Time Out
Status
```

Example:

```text
============================================================
Today's Attendance
============================================================

ID   Employee       Date         Time In    Time Out   Status
1    Jose Navoa     2026-10-07   08:02:15   -         Late
2    Juan Santos    2026-10-07   07:55:10   17:01:22 Present
```

Employees who have not clocked out yet display:

```text
-
```

under the Time Out column.

---

# Attendance Status

The Python version currently uses attendance status based on the employee's Clock In time.

Available statuses include:

```text
Present
Late
```

For example:

```text
Clock In: 07:55
Status: Present
```

and:

```text
Clock In: 08:15
Status: Late
```

The attendance record remains associated with the employee after Clock Out.

---

# Attendance Reports

The Python version now includes a dedicated **Reports** section.

The Reports page allows users to review attendance records using different filters.

The report system includes:

* Date range filtering
* Employee filtering
* Today's report
* Attendance record listing
* Total record count
* Present count
* Late count
* Completed count
* Report generation
* Attendance history

---

# Report Date Filtering

Users can specify a start date and end date.

The date format used by the report system is:

```text
YYYY-MM-DD
```

Example:

```text
Start Date: 2026-10-01
End Date:   2026-10-07
```

The system then displays attendance records within that date range.

The system also validates the selected dates.

For example, the start date cannot be later than the end date.

---

# Employee Report Filtering

Reports can also be filtered by employee.

The employee filter provides:

```text
All Employees
```

as well as individual employees.

Example:

```text
Employee:
[ Jose Navoa ]
```

The generated report will then display attendance records associated with the selected employee.

This makes it easier to review an individual employee's attendance history.

---

# Today's Report

The Reports page includes a **Today** button.

Selecting Today automatically sets both dates to the current date.

Example:

```text
Start Date: 2026-10-07
End Date:   2026-10-07
Employee:   All Employees
```

The system then generates the attendance records for the current day.

---

# Report Summary

The Reports page provides summary cards based on the selected filters.

The current summary includes:

```text
Total Records
Present
Late
Completed
```

Example:

```text
Total Records     10
Present            7
Late               3
Completed          8
```

These values are automatically calculated from the attendance records returned by the selected report filters.

---

# Report Table

Generated reports display attendance information in a table.

The table includes:

| ID | Employee    | Date       | Time In  | Time Out | Status  |
| -- | ----------- | ---------- | -------- | -------- | ------- |
| 10 | Jose Navoa  | 2026-10-07 | 08:02:15 | 17:03:21 | Late    |
| 9  | Juan Santos | 2026-10-07 | 07:55:10 | 17:01:22 | Present |

If no attendance records match the selected filters, the system displays:

```text
No attendance records found.
```

---

# Attendance Validation

The system includes validation to help prevent incorrect attendance records.

Examples include:

* Preventing Clock In without selecting an employee
* Preventing duplicate attendance records for the same employee and date
* Preventing Clock Out without a Clock In record
* Preventing duplicate Clock Out
* Checking whether employees exist
* Validating employee names
* Validating report dates
* Preventing an invalid date range
* Confirming employee deletion
* Handling database errors
* Handling empty search results

These controls help keep attendance information organized and consistent.

---

# Database

The Python version uses **SQLite** for persistent data storage.

The database stores employee and attendance information.

The database is accessed through:

```text
database.py
```

The main database file is:

```text
company_attendance.db
```

The database allows information to remain available even after closing and reopening the application.

---

# Python Desktop Version

The Python version is a desktop application built using:

* Python
* CustomTkinter
* SQLite
* datetime

The application uses a modular structure where different features are separated into different Python files.

The main modules are:

```text
main.py
database.py
dashboard.py
employees.py
attendance.py
reports.py
```

This structure makes the application easier to understand, maintain, debug, and expand.

---

# Python Project Structure

```text
python-version/
│
├── main.py
├── database.py
├── dashboard.py
├── employees.py
├── attendance.py
├── reports.py
└── company_attendance.db
```

---

# Python Modules

## `main.py`

The main entry point of the Python application.

Responsible for:

* Starting the application
* Creating the main window
* Creating the sidebar
* Creating the content area
* Managing navigation
* Loading application pages
* Switching between pages
* Closing the application

The main navigation includes:

```text
Dashboard
Attendance
Employees
Reports
Exit
```

---

## `database.py`

Handles SQLite database operations.

Responsible for:

* Creating database tables
* Connecting to SQLite
* Storing employee information
* Storing attendance information
* Retrieving employee records
* Searching employee records
* Updating employee records
* Deleting employee records
* Creating attendance records
* Retrieving attendance records
* Updating Clock Out information
* Retrieving today's attendance
* Filtering attendance information

The database module keeps database operations separate from the graphical interface.

---

## `dashboard.py`

Contains the main Dashboard interface.

Responsible for:

* Dashboard layout
* Current date display
* Employee statistics
* Today's attendance statistics
* Recent attendance records
* Attendance overview

Current dashboard statistics include:

```text
Total Employees
Present Today
Late Today
Absent Today
```

---

## `employees.py`

Handles Employee Management.

Responsible for:

* Adding employees
* Viewing employees
* Searching employees
* Editing employees
* Deleting employees
* Refreshing employee records
* Validating employee information

Employee records contain:

```text
ID
Name
Position
Department
Contact
```

---

## `attendance.py`

Handles daily attendance.

Responsible for:

* Selecting employees
* Clock In
* Clock Out
* Recording dates
* Recording times
* Determining attendance status
* Displaying today's attendance
* Preventing duplicate attendance records
* Preventing invalid Clock Out operations
* Refreshing attendance information

The attendance table contains:

```text
ID
Employee
Date
Time In
Time Out
Status
```

---

## `reports.py`

Handles attendance reports.

Responsible for:

* Generating reports
* Filtering by start date
* Filtering by end date
* Filtering by employee
* Viewing today's reports
* Displaying attendance history
* Calculating report summaries
* Counting total records
* Counting Present records
* Counting Late records
* Counting Completed records

The Reports module provides a dedicated way to analyze attendance information without modifying the original attendance records.

---

# Python Application Architecture

The Python version follows a modular application structure:

```text
                         main.py
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
        dashboard.py   employees.py   attendance.py
             │              │              │
             │              │              │
             └──────────────┼──────────────┘
                            │
                            ▼
                       database.py
                            │
                            ▼
                  company_attendance.db

                            │
                            ▼
                       reports.py
```

The modules have separate responsibilities while sharing the same database.

---

# Application Navigation

The Python application uses a sidebar for navigation.

```text
┌─────────────────────┐
│   ATTENDANCE        │
│      SYSTEM         │
├─────────────────────┤
│                     │
│   Dashboard         │
│   Attendance        │
│   Employees         │
│   Reports           │
│                     │
│                     │
│                     │
│   Exit              │
└─────────────────────┘
```

Selecting a navigation button clears the current content area and loads the selected page.

---

# Employee Workflow

The employee-management workflow is:

```text
Employees
    ↓
Add Employee
    ↓
Enter Employee Information
    ↓
Save Employee
    ↓
Employee Stored in SQLite
    ↓
Employee Appears in Employee List
```

Existing employees can then be:

```text
Search
   ↓
View
   ↓
Edit
   ↓
Delete
```

---

# Attendance Workflow

The attendance workflow is:

```text
Select Employee
       ↓
   Clock In
       ↓
Check Existing Record
       ↓
Record Date and Time
       ↓
Determine Status
       ↓
   Work Session
       ↓
   Clock Out
       ↓
Update Attendance Record
       ↓
Attendance Completed
```

---

# Reports Workflow

The report workflow is:

```text
Open Reports
      ↓
Select Date Range
      ↓
Select Employee
      ↓
Generate Report
      ↓
Retrieve Matching Records
      ↓
Calculate Summary
      ↓
Display Attendance Report
```

Users can also select:

```text
Today
```

to immediately generate a report for the current date.

---

# Web Version

The project also includes a browser-based **Web Version** of the Company Attendance System.

The Web Version uses:

* HTML
* CSS
* JavaScript
* Browser Local Storage

The web application is designed to run directly inside a modern web browser.

The Web Version follows the same general attendance-management concept as the Python application.

---

# Web Version Features

The Web Version includes the major functionality of the attendance system, including:

* Dashboard
* Employee management
* Employee records
* Clock In
* Clock Out
* Attendance records
* Attendance history
* Date and time recording
* Attendance status
* Browser-based interface
* Responsive layout
* Interactive user interface
* Client-side data storage

---

# Web Project Structure

```text
web-version/
│
├── index.html
├── style.css
└── script.js
```

### `index.html`

Contains the structure of the web application.

Responsible for:

* Dashboard layout
* Navigation
* Employee sections
* Attendance sections
* Buttons
* Forms
* Tables
* User interface elements

### `style.css`

Controls the visual appearance of the Web Version.

Responsible for:

* Layout
* Typography
* Spacing
* Colors
* Cards
* Buttons
* Tables
* Navigation
* Responsive design

### `script.js`

Controls the functionality of the Web Version.

Responsible for:

* Employee management
* Clock In
* Clock Out
* Attendance records
* Date and time handling
* UI updates
* Data storage
* User interactions
* Validation
* Dashboard updates

---

# Web Data Storage

The Web Version uses browser-based storage for its data.

The application can use **Local Storage** to retain information inside the user's browser.

Basic workflow:

```text
User opens website
       ↓
JavaScript loads stored data
       ↓
User manages employees
       ↓
Employee clocks in
       ↓
Attendance record is created
       ↓
Employee clocks out
       ↓
Attendance record is updated
       ↓
Data is saved
```

The Web Version's Local Storage is separate from the SQLite database used by the Python version.

---

# Python Version vs Web Version

Both versions implement the same general attendance-management concept but use different technologies.

| Feature            | Python Version      | Web Version               |
| ------------------ | ------------------- | ------------------------- |
| Platform           | Desktop             | Browser                   |
| Language           | Python              | JavaScript                |
| Interface          | CustomTkinter       | HTML/CSS                  |
| Database           | SQLite              | Browser Local Storage     |
| Dashboard          | Yes                 | Yes                       |
| Employees          | Yes                 | Yes                       |
| Employee Search    | Yes                 | Yes                       |
| Employee Delete    | Yes                 | Yes                       |
| Clock In           | Yes                 | Yes                       |
| Clock Out          | Yes                 | Yes                       |
| Attendance Records | Yes                 | Yes                       |
| Attendance Reports | Yes                 | Depends on Web Version    |
| Working Hours      | Attendance tracking | Depends on implementation |
| Today's Records    | Yes                 | Yes                       |
| Statistics         | Yes                 | Yes                       |
| Persistent Storage | SQLite              | Local Storage             |
| Internet Required  | No                  | No for local version      |

---

# Programming Concepts Demonstrated

This project demonstrates several programming and software-development concepts.

## Variables and Data Types

Used for:

* Employee information
* Attendance information
* Dates
* Times
* Status values
* Database records

## Functions

Used to organize operations such as:

* Adding employees
* Searching employees
* Editing employees
* Deleting employees
* Clocking in
* Clocking out
* Retrieving attendance
* Generating reports
* Filtering reports
* Calculating report summaries

## Modules

The Python application separates functionality into multiple files.

```text
main.py
database.py
dashboard.py
employees.py
attendance.py
reports.py
```

## CRUD Operations

The project demonstrates:

```text
Create
Read
Update
Delete
```

Examples:

```text
Create → Add Employee
Read   → View Employee / Attendance
Update → Edit Employee / Clock Out
Delete → Delete Employee
```

## Event-Driven Programming

The application responds to user actions such as:

* Clicking buttons
* Selecting employees
* Entering search terms
* Adding employees
* Editing employees
* Deleting employees
* Clocking in
* Clocking out
* Generating reports

## Database Operations

The Python version demonstrates:

* SQLite connections
* SQL queries
* INSERT operations
* SELECT operations
* UPDATE operations
* DELETE operations
* JOIN operations
* Filtering database records

## Date and Time Handling

The system uses Python's `datetime` module to:

* Record the current date
* Record Clock In time
* Record Clock Out time
* Determine whether an employee is late
* Filter attendance records by date

---

# Installation and Setup

## Python Version

### Requirements

Python must be installed on the computer.

Check the Python installation:

```bash
python --version
```

If Python is not recognized, try:

```bash
py --version
```

### Install CustomTkinter

```bash
pip install customtkinter
```

### Run the Application

Navigate to the Python directory:

```bash
cd python-version
```

Then run:

```bash
python main.py
```

If `python` does not work but `py` does:

```bash
py main.py
```

The SQLite database will be used by the application for persistent storage.

---

# Running the Web Version

The Web Version does not require Python.

Navigate to:

```text
web-version/
```

Then open:

```text
index.html
```

in a modern web browser.

The project can also be opened using Visual Studio Code and a local development extension such as Live Server.

---

# Troubleshooting

## Python is not recognized

If Windows shows:

```text
Python was not found
```

Try:

```bash
py --version
```

Then:

```bash
py main.py
```

---

## CustomTkinter is not installed

If you see:

```text
ModuleNotFoundError: No module named 'customtkinter'
```

Run:

```bash
pip install customtkinter
```

Then:

```bash
python main.py
```

---

## No Employees Are Available

Make sure at least one employee has been added through the **Employees** page.

The Attendance page gets its employee list from the SQLite database.

---

## Employee Cannot Clock In

Check that:

1. An employee has been selected.
2. The employee exists in the database.
3. The employee does not already have an attendance record for today.

---

## Employee Cannot Clock Out

Check that:

1. An employee has been selected.
2. The employee has an attendance record for today.
3. The employee has not already clocked out.

---

## Reports Show No Records

Check:

1. The selected date range.
2. The selected employee.
3. Whether attendance records exist for the selected dates.

The date format must be:

```text
YYYY-MM-DD
```

Example:

```text
2026-10-07
```

---

## Database Errors

Make sure the application is using the correct database file:

```text
company_attendance.db
```

The database tables and columns must match the structure expected by the Python modules.

---

# Future Improvements

The current system provides the core functionality of an employee attendance application. Future versions can expand the system further.

## Attendance

Possible improvements:

* Automatic working-hours calculation
* Late arrival detection improvements
* Early departure detection
* Overtime calculation
* Break tracking
* Absence tracking
* Attendance status improvements
* Daily summaries
* Weekly summaries
* Monthly summaries

## Employee Management

Possible improvements:

* Employee profile pictures
* Additional employee information
* Employee status
* More advanced search
* Department filtering
* Position filtering

## Reports

Possible improvements:

* CSV export
* Excel export
* PDF reports
* Monthly attendance reports
* Individual employee reports
* Department reports
* Payroll-ready reports
* Graphical attendance statistics

## Authentication

Possible improvements:

* Admin login
* Employee login
* Role-based permissions
* Password protection
* Account management

## Web Improvements

Possible improvements:

* Backend API
* Cloud database
* User authentication
* Multi-user support
* Real-time attendance
* Server-side database
* Online synchronization
* Admin dashboard
* Web deployment

## Advanced Attendance

Possible improvements:

* QR code attendance
* RFID integration
* Biometric attendance
* Location-based attendance
* Email notifications
* Automatic backups

---

# Planned System Architecture

A future full-stack version could evolve from the current two implementations into a centralized system.

```text
                  COMPANY ATTENDANCE SYSTEM
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
       Desktop Application          Web Application
              │                           │
              │                           │
              └─────────────┬─────────────┘
                            ▼
                       Backend API
                            │
                            ▼
                       Main Database
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
        Employees       Attendance       Reports
```

This would allow multiple users and devices to work with the same centralized attendance data.

---

# Learning Outcomes

This project provides practical experience with:

* Python programming
* JavaScript programming
* HTML
* CSS
* GUI development
* Web development
* SQLite
* Local Storage
* Database management
* CRUD operations
* Modular programming
* Event-driven programming
* Date and time handling
* Input validation
* Error handling
* SQL queries
* Database relationships
* Report generation
* Data filtering
* Data persistence
* Git and GitHub project organization

---

# Project Status

**Current Status: Expanded Python Desktop Version + Web Version**

The Python version is now organized into six main modules:

```text
main.py
database.py
dashboard.py
employees.py
attendance.py
reports.py
```

The application currently provides:

```text
Dashboard
    │
    ├── Total Employees
    ├── Present Today
    ├── Late Today
    ├── Absent Today
    └── Recent Attendance
             │
             ▼
Employees
    │
    ├── Add Employee
    ├── Search Employee
    ├── Edit Employee
    ├── Delete Employee
    └── Refresh
             │
             ▼
Attendance
    │
    ├── Select Employee
    ├── Clock In
    ├── Clock Out
    ├── Today's Attendance
    └── Attendance Status
             │
             ▼
Reports
    │
    ├── Date Range
    ├── Employee Filter
    ├── Today's Report
    ├── Total Records
    ├── Present
    ├── Late
    └── Completed
```

The system uses SQLite to persist employee and attendance information.

The Web Version provides a separate browser-based implementation using HTML, CSS, JavaScript, and Local Storage.

---

# Purpose

The purpose of this project is to create a practical employee attendance system while applying programming and software-development concepts.

Instead of creating separate small programming exercises, this project combines multiple concepts into one functional application.

The project demonstrates how the same system can be implemented for different platforms.

```text
                 COMPANY ATTENDANCE SYSTEM
                           │
             ┌─────────────┴─────────────┐
             │                           │
             ▼                           ▼
      Python Desktop                Web Application
             │                           │
       CustomTkinter              HTML + CSS + JS
             │                           │
          SQLite                  Local Storage
             │                           │
             └─────────────┬─────────────┘
                           ▼
                  Employee Attendance
                       Management
```

---

# Author

**Jose Navoa**

Information Technology Student

---

# License

This project is intended for **educational and personal use**.

See the `LICENSE` file included in the repository for additional information.
