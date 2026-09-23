# Company Attendance System

A complete **Employee Attendance Management System** developed with two versions: a **Python Desktop Application** and a **Web Application**.

The system is designed to help companies manage employee information and track daily attendance through **Clock In** and **Clock Out** functionality.

The project demonstrates how the same core attendance-management concept can be implemented across different platforms while using appropriate technologies for each version.

---

## Overview

The **Company Attendance System** provides a centralized way to manage employees and record their attendance.

The project currently contains two available versions:

| Version        | Technologies                  | Platform    |
| -------------- | ----------------------------- | ----------- |
| Python Version | Python, CustomTkinter, SQLite | Desktop     |
| Web Version    | HTML, CSS, JavaScript         | Web Browser |

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
```

The Python version provides a desktop-based implementation, while the Web version provides a browser-based implementation with a modern web interface.

---

# Features

## Dashboard

The dashboard serves as the main control center of the attendance system.

It provides access to the major sections of the application, including:

* Dashboard
* Employee Management
* Clock In
* Clock Out
* Attendance Records
* Attendance statistics
* Navigation between system sections
* Live date and time display
* Current employee count
* Currently working employee count
* Clocked-out employee count
* Today's attendance record count
* Quick attendance controls
* Today's attendance table
* Refresh functionality
* Attendance summary
* Total working hours
* Average working hours
* Employee attendance overview

The dashboard is designed to give users a quick overview of the current attendance system.

The Python dashboard includes statistic cards that provide a quick summary of the current attendance situation.

Example:

```text
Total Employees       10
Currently Working      4
Clocked Out            6
Today's Records       10
```

---

# Employee Management

The Employee Management section allows users to maintain employee information.

Features include:

* Add employees
* View employees
* Manage employee records
* Search employees
* Display all employees
* Delete selected employees
* Select employees for attendance
* Associate employees with attendance records
* Organize employee information
* Employee ID management
* Full name management
* Department management
* Position management
* Employee status management
* Prevent duplicate employee IDs
* Clear employee form
* Refresh employee list

Employee information is connected to attendance records so that every clock-in and clock-out can be associated with the correct employee.

Each employee can contain:

```text
Employee ID
Full Name
Department
Position
```

Example:

```text
Employee ID: EMP001
Full Name: Jose Navoa
Department: IT
Position: IT Assistant
```

---

# Add Employee

The system provides a dedicated form for adding new employees.

The user can enter:

```text
Employee ID
Full Name
Department
Position
```

After successfully adding an employee, the employee list is refreshed automatically.

The form can also be cleared after a successful registration.

The system checks for duplicate Employee IDs before creating a new employee.

Example:

```text
Employee ID: EMP001
Full Name: Jose Navoa
Department: IT
Position: IT Assistant

[ Add Employee ]
[ Clear ]
```

---

# Employee Search

The Python desktop version includes an employee search function.

Users can search employee records using information such as:

```text
Employee ID
Employee Name
```

The search system allows users to quickly locate an employee without manually looking through the entire employee list.

Users can also use **Show All** to return to the complete employee list.

Example:

```text
Search: Jose

EMP001 | Jose Navoa | IT | IT Assistant
```

---

# Delete Employee

The Employee Management section includes a delete function.

Users can select an employee from the employee table and remove the employee from the system.

Before deleting an employee, the system can display a confirmation message.

Example:

```text
Are you sure you want to delete this employee?
```

This helps prevent accidental deletion of employee information.

---

# Clock In

The Clock In feature records the beginning of an employee's work session.

When an employee clocks in, the system:

1. Identifies the employee.
2. Checks whether the employee exists.
3. Checks whether the employee already has an active attendance session.
4. Gets the current date.
5. Gets the current time.
6. Creates an attendance record.
7. Stores the clock-in information.
8. Associates the attendance record with the employee.
9. Updates the attendance status.
10. Refreshes the attendance information.

Example:

```text
Employee: Jose Navoa
Date: September 3, 2026
Clock In: 08:02 AM
Status: Currently Working
```

The system is designed to prevent unnecessary duplicate clock-ins for an employee who already has an active attendance session.

If an employee is not registered, the system displays an appropriate message instead of creating an invalid attendance record.

---

# Clock Out

The Clock Out feature records when an employee finishes their work session.

When an employee clocks out, the system:

1. Identifies the employee.
2. Checks whether the employee exists.
3. Finds the active attendance session.
4. Gets the current time.
5. Calculates the total working time.
6. Updates the attendance record.
7. Saves the clock-out information.
8. Changes the attendance status to completed.
9. Refreshes the attendance information.

Example:

```text
Employee: Jose Navoa
Date: September 3, 2026
Clock In: 08:02 AM
Clock Out: 05:04 PM
Working Hours: 9h 2m 0s
Status: Completed
```

This creates a complete attendance session containing both the clock-in and clock-out times.

The system also prevents an employee from clocking out when there is no active clock-in session.

---

# Quick Attendance

The Python Dashboard and Attendance pages include a **Quick Attendance** section.

Users can enter an employee ID and immediately perform attendance actions.

Available actions include:

* Clock In
* Clock Out
* Clear

Example workflow:

```text
Enter Employee ID
       ↓
    Clock In
       ↓
Employee starts work
       ↓
    Clock Out
       ↓
Working hours calculated
       ↓
Attendance completed
```

This makes common attendance actions faster and easier to access.

---

# Working Hours Calculation

The Python version calculates the amount of time an employee worked during a completed attendance session.

The calculation is based on:

```text
Clock Out Time
       -
Clock In Time
       =
Total Working Time
```

The result is displayed using hours, minutes, and seconds.

Example:

```text
Clock In:      08:00:00 AM
Clock Out:     05:00:00 PM

Working Hours:
9h 0m 0s
```

The system can also use the recorded attendance information to calculate total and average working hours.

---

# Attendance Records

The Attendance section allows users to review recorded attendance.

An attendance record can contain:

* Employee ID
* Employee name
* Attendance date
* Clock-in time
* Clock-out time
* Working hours
* Attendance status

Example:

| Employee ID | Employee   | Clock In | Clock Out | Working Hours | Status    |
| ----------- | ---------- | -------- | --------- | ------------- | --------- |
| EMP001      | Jose Navoa | 08:02 AM | 05:04 PM  | 9h 2m 0s      | Completed |
| EMP002      | Employee 2 | 08:15 AM | 05:10 PM  | 8h 55m 0s     | Completed |

Attendance information is retained so previous records can be reviewed.

---

# Attendance Search

The Python Attendance page includes a search feature for attendance records.

Users can search attendance information using:

```text
Employee ID
Employee Name
```

The page also provides options to:

* Search attendance
* View today's attendance
* Show all attendance records
* Refresh attendance information
* Filter attendance records

This makes it easier to locate specific attendance records.

---

# Today's Attendance

The Python version includes a **Today** view that displays attendance records for the current date.

This allows users to quickly see who has:

* Clocked in
* Clocked out
* Completed a work session
* Remained currently working

The dashboard also displays today's attendance records automatically.

Example:

```text
========================================
        TODAY'S ATTENDANCE
========================================

EMP001 | Jose Navoa
Clock In: 08:02 AM
Clock Out: 05:04 PM
Hours: 9h 2m 0s
Status: Completed

EMP002 | Employee 2
Clock In: 08:15 AM
Status: Currently Working
```

---

# Currently Working Employees

The system can identify employees who currently have an active attendance session.

This allows the dashboard and attendance pages to show employees who are currently working.

Example:

```text
========================================
       CURRENTLY WORKING
========================================

EMP001 | Jose Navoa
Clock In: 08:02 AM

EMP003 | Mark Santos
Clock In: 08:21 AM
```

This information is also used by the dashboard's **Currently Working** statistic.

---

# Attendance Summary

The system provides attendance summaries based on recorded employee attendance.

A summary can include:

* Total attendance records
* Completed attendance records
* Currently working employees
* Total working hours
* Average working hours
* Employee attendance totals

Example:

```text
========================================
         ATTENDANCE SUMMARY
========================================

Employee: Jose Navoa
Employee ID: EMP001

Total Records: 15
Completed Records: 14
Currently Working: No
Total Hours: 126h 30m
Average Hours: 9h 2m
```

---

# Attendance Statistics

The system provides statistics that summarize the current attendance situation.

Statistics can include:

```text
Total Employees
Currently Working
Clocked Out
Today's Records
Total Attendance Records
Completed Records
Total Working Hours
Average Working Hours
```

Example:

```text
========================================
        ATTENDANCE STATISTICS
========================================

Total Employees: 10
Currently Working: 4
Clocked Out: 6
Today's Records: 10
Completed Records: 8
Total Working Hours: 72h 30m
```

---

# Live Date and Time

The Python dashboard includes a live clock that updates automatically.

The dashboard displays:

```text
Current Date
Current Time
```

The time is refreshed continuously while the application is running.

This provides a real-time view of the current system time for attendance operations.

---

# Refresh Functionality

The Python version includes refresh functionality for different sections of the application.

Refresh actions can update:

* Dashboard statistics
* Employee list
* Attendance records
* Today's attendance
* Search results
* Currently working employees

This allows the interface to display the most recent information without restarting the application.

---

# Attendance Validation

The system includes validation to help prevent incorrect attendance records.

Examples include:

* Preventing empty employee IDs
* Preventing duplicate active clock-ins
* Preventing clock-out without an active attendance session
* Checking whether an employee exists
* Validating employee information
* Preventing duplicate employee IDs
* Confirming employee deletion
* Maintaining valid attendance sessions
* Checking required employee fields
* Handling invalid searches
* Handling missing employee records

These controls help keep attendance information organized and consistent.

---

# Attendance Status

Attendance records can have different statuses depending on the employee's current work session.

Common statuses include:

```text
Currently Working
Completed
```

Example:

```text
EMP001 | Jose Navoa | Currently Working
EMP002 | John Cruz | Completed
```

The status changes automatically when an employee clocks out.

---

# Attendance Record Management

The expanded attendance functionality allows the system to manage attendance information more effectively.

Attendance management includes:

* Creating attendance records
* Viewing attendance records
* Searching attendance records
* Filtering attendance records
* Viewing today's attendance
* Viewing all attendance
* Identifying active attendance sessions
* Calculating working hours
* Updating completed attendance records
* Removing attendance records where supported
* Refreshing attendance information

---

# Python Desktop Version

The Python version is a desktop application built using **Python and CustomTkinter**.

It provides a graphical interface that allows users to manage employees and attendance from a desktop environment.

The Python version was expanded into a more structured **multi-page desktop application** rather than keeping all functionality inside a single file.

## Technologies

* Python
* CustomTkinter
* SQLite
* `datetime`
* Tkinter Treeview

## Python Features

The Python version includes:

* Desktop graphical interface
* Dashboard
* Employee management
* Add employee
* Employee search
* Employee deletion
* Employee validation
* Clock In
* Clock Out
* Quick attendance controls
* Attendance records
* Attendance search
* Attendance filtering
* Today's attendance view
* Show all attendance records
* Currently working employees
* Attendance summary
* Attendance statistics
* Automatic working-hours calculation
* Live date and time
* SQLite database
* Persistent data storage
* Input validation
* Attendance session management
* Modular Python structure
* Navigation between application pages
* Confirmation dialogs
* Error handling
* Refresh functionality

---

# Python Dashboard Updates

The Python dashboard was expanded to provide more useful attendance information.

The dashboard now includes:

## Statistics

* Total Employees
* Currently Working
* Clocked Out
* Today's Records
* Completed Attendance Records
* Total Working Hours
* Average Working Hours

## Quick Attendance

* Employee ID input
* Clock In button
* Clock Out button
* Clear button

## Today's Attendance

The dashboard includes a table showing today's attendance records.

The table can display:

```text
Employee ID
Employee Name
Clock In
Clock Out
Working Hours
Status
```

## Live Clock

The dashboard also displays the current date and time and updates automatically.

## Refresh

The dashboard can refresh its statistics and today's attendance information.

---

# Python Employee Page Updates

The Employee Management page was expanded into a dedicated interface.

It now includes a form for:

```text
Add New Employee
       ↓
Employee ID
Full Name
Department
Position
       ↓
Add Employee
```

The employee list displays:

```text
Employee ID
Full Name
Department
Position
```

Additional controls include:

* Search
* Show All
* Delete Selected Employee
* Clear form after successful registration
* Refresh employee list
* Duplicate Employee ID validation
* Required-field validation
* Employee selection

---

# Python Attendance Page Updates

The Attendance page was expanded into a dedicated attendance-management interface.

It includes a **Quick Attendance** section for:

* Clock In
* Clock Out
* Clear

It also includes an attendance history section with:

* Search
* Today
* Show All
* Refresh
* Attendance filtering

The attendance table displays:

```text
Employee ID
Employee Name
Clock In
Clock Out
Working Hours
Status
```

The Attendance page can also identify employees who are currently working.

This creates a more complete attendance-management workflow.

---

# Python Attendance Functions

The expanded Python attendance system includes functions for:

```text
Employee Management
        │
        ├── Add Employee
        ├── Search Employee
        ├── Show All Employees
        ├── Delete Employee
        └── Validate Employee
                 │
                 ▼
          Attendance Management
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
     Clock In Clock Out Search
        │        │        │
        └────────┼────────┘
                 ▼
        Attendance Records
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
       Today   Summary   Statistics
                 │
                 ▼
          Working Hours
```

These functions allow the application to handle the complete basic attendance workflow.

---

# Python Modular Architecture

The Python version separates different parts of the application into individual modules.

```text
main.py
   │
   ├── dashboard.py
   │
   ├── employees.py
   │
   ├── attendance.py
   │
   └── database.py
```

This makes the application easier to:

* Understand
* Maintain
* Debug
* Expand
* Organize
* Modify

Each file is responsible for a specific part of the system.

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
└── company_attnce.db
```

### `main.py`

The main entry point of the Python application.

Responsible for:

* Starting the application
* Initializing the GUI
* Creating the main window
* Creating the navigation sidebar
* Loading application pages
* Switching between pages
* Managing application navigation
* Starting the main event loop

The main navigation includes:

```text
Dashboard
Employees
Attendance
Exit Application
```

### `database.py`

Handles SQLite database operations.

Responsible for:

* Creating the database
* Creating tables
* Connecting to SQLite
* Storing employee information
* Storing attendance information
* Retrieving employees
* Searching employees
* Deleting employees
* Creating attendance records
* Finding active attendance sessions
* Updating attendance after Clock Out
* Retrieving today's attendance
* Searching attendance
* Calculating dashboard statistics
* Calculating working hours
* Retrieving attendance summaries

The database provides persistent storage so information remains available after restarting the application.

### `dashboard.py`

Contains the main dashboard interface.

Responsible for:

* Dashboard layout
* Live date and time
* Attendance statistics
* Attendance summary
* Quick attendance controls
* Today's attendance table
* Dashboard refresh
* Clock In
* Clock Out
* Currently working employee information

### `employees.py`

Handles employee management.

Responsible for:

* Adding employees
* Displaying employees
* Searching employees
* Showing all employees
* Deleting selected employees
* Managing employee information
* Validating employee input
* Preventing duplicate employee IDs
* Clearing the employee form
* Refreshing the employee list

### `attendance.py`

Handles attendance functionality.

Responsible for:

* Clock In
* Clock Out
* Recording dates
* Recording times
* Calculating working hours
* Displaying attendance records
* Searching attendance
* Viewing today's attendance
* Viewing all attendance
* Managing attendance sessions
* Displaying attendance status
* Refreshing attendance records
* Showing currently working employees

### `company_attnce.db`

The SQLite database used to store persistent application data.

The Python version uses SQLite tables for employee and attendance information.

---

# Python Database Structure

The Python version uses SQLite to store employee and attendance information.

The main data is organized around:

```text
Employees
    │
    ├── Employee ID
    ├── Full Name
    ├── Department
    └── Position
             │
             ▼
       Attendance
             │
      ┌──────┼────────┐
      ▼      ▼        ▼
   Clock In Clock Out Working Hours
```

The attendance system connects employee information with attendance records.

Attendance records can also contain a status that identifies whether the employee is currently working or has completed the work session.

---

# Web Version

The project also includes a **browser-based Web Version** of the Company Attendance System.

The Web Version provides the same core attendance concept as the Python application while using standard web technologies.

## Technologies

* HTML
* CSS
* JavaScript
* Browser Local Storage

The web application is designed to run directly inside a modern web browser.

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

The Web Version is designed to make the attendance system accessible without requiring the user to run a Python desktop application.

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
* Animations and transitions

### `script.js`

Controls the functionality and interaction of the Web Version.

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

The system can use **Local Storage** to retain information inside the user's browser.

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

This allows the Web Version to maintain information even after the browser page is refreshed.

> The Web Version's local storage is intended for a browser-based application and is different from the SQLite database used by the Python version.

---

# Python Version vs Web Version

Both versions implement the same general attendance-management concept but use different technologies.

| Feature            | Python Version  | Web Version           |
| ------------------ | --------------- | --------------------- |
| Platform           | Desktop         | Browser               |
| Language           | Python          | JavaScript            |
| Interface          | CustomTkinter   | HTML/CSS              |
| Database           | SQLite          | Browser Local Storage |
| Dashboard          | Yes             | Yes                   |
| Employees          | Yes             | Yes                   |
| Employee Search    | Yes             | Yes                   |
| Employee Delete    | Yes             | Yes                   |
| Clock In           | Yes             | Yes                   |
| Clock Out          | Yes             | Yes                   |
| Working Hours      | Yes             | Yes                   |
| Attendance Records | Yes             | Yes                   |
| Attendance Search  | Yes             | Yes                   |
| Today's Records    | Yes             | Yes                   |
| Statistics         | Yes             | Yes                   |
| Live Clock         | Yes             | Yes                   |
| Persistent Storage | SQLite          | Local Storage         |
| Installation       | Python required | Browser required      |
| Internet Required  | No              | No for local version  |

---

# Why Two Versions?

The project contains two versions to demonstrate how the same software concept can be developed using different technologies.

## Python Version

The Python version demonstrates:

* Python programming
* GUI development
* SQLite
* Object-oriented programming
* Database management
* CRUD operations
* Desktop application development
* Modular application design
* Event-driven programming
* Date and time handling

## Web Version

The Web Version demonstrates:

* HTML
* CSS
* JavaScript
* DOM manipulation
* Browser storage
* Responsive web design
* Web application development
* Interactive user interfaces

Together, the two versions demonstrate the difference between **desktop application development and web application development**.

---

# Attendance Workflow

The complete attendance workflow is:

```text
                    COMPANY ATTENDANCE SYSTEM
                              │
                              ▼
                         Dashboard
                              │
                ┌─────────────┴─────────────┐
                ▼                           ▼
       Employee Management           Attendance
                │                           │
                ▼                           ▼
        Add / Search Employee          Clock In
                │                           │
                ▼                           ▼
          Select Employee             Work Session
                                            │
                                            ▼
                                         Clock Out
                                            │
                                            ▼
                                  Calculate Working Hours
                                            │
                                            ▼
                                    Attendance Record
                                            │
                              ┌─────────────┴─────────────┐
                              ▼                           ▼
                       Attendance Search           Attendance Summary
                              │                           │
                              ▼                           ▼
                       Today's Records             Statistics
```

---

# Attendance Validation

The system is designed to help prevent common attendance problems.

Examples include:

* Preventing unnecessary duplicate clock-ins
* Preventing clock-out without an active attendance session
* Associating attendance with the correct employee
* Automatically recording the current date
* Automatically recording the current time
* Maintaining completed attendance records
* Validating employee information
* Preventing duplicate employee IDs
* Validating required fields
* Checking employee existence
* Maintaining valid attendance status

These controls help keep attendance information organized and consistent.

---

# Database and Data Management

The project uses different storage technologies depending on the version.

## Python

The Python version uses:

```text
SQLite
```

SQLite provides local persistent database storage.

It can contain tables for:

```text
Employees
     │
     └── Employee ID
              │
              ▼
       Attendance Records
              │
       ┌──────┼──────┐
       ▼      ▼      ▼
     Date  Clock In Clock Out
```

The Python version also uses the attendance information to calculate working hours and display dashboard statistics.

## Web

The Web Version uses:

```text
Browser Local Storage
```

This allows the application to save data locally in the browser.

A future production version could replace Local Storage with a server-side database and API.

---

# Technologies Used

## Python Version

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| Python           | Main programming language |
| CustomTkinter    | Desktop GUI               |
| SQLite           | Database                  |
| datetime         | Date and time             |
| Tkinter Treeview | Data tables               |

## Web Version

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| HTML          | Application structure     |
| CSS           | Design and layout         |
| JavaScript    | Application functionality |
| Local Storage | Browser data persistence  |

---

# Programming Concepts Demonstrated

This project demonstrates several programming and software development concepts.

### Variables and Data Types

Used for:

* Employee information
* Attendance information
* Dates
* Times
* Application states
* Working-hour calculations

### Functions

Used to organize operations such as:

* Adding employees
* Searching employees
* Deleting employees
* Clocking in
* Clocking out
* Retrieving attendance
* Updating records
* Calculating working hours
* Calculating attendance summaries
* Refreshing application data

### Object-Oriented Programming

Used primarily in the Python version to organize GUI components and application functionality.

### Modules

The Python version separates functionality into multiple files.

### CRUD Operations

The project demonstrates:

```text
Create
Read
Update
Delete
```

For example:

* Create employee
* Read employee information
* Update attendance after Clock Out
* Delete employee records where supported

### Event-Driven Programming

Both versions respond to user actions such as:

* Clicking buttons
* Entering employee information
* Searching records
* Clocking in
* Clocking out
* Selecting records
* Refreshing information

### Date and Time Handling

The system automatically records attendance dates and times and calculates working-session duration.

### Input Validation

The application checks user input before performing important operations.

### Database Operations

The Python version demonstrates:

* SQLite connections
* SQL queries
* Insert operations
* Select operations
* Update operations
* Delete operations

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

in a modern browser.

You can also run it through **Visual Studio Code** using a local development extension such as Live Server.

Basic process:

```text
Open Project in VS Code
        ↓
Open web-version
        ↓
Open index.html
        ↓
Run with a browser
        ↓
Use the Attendance System
```

---

# Running the Project in Visual Studio Code

## Python Version

Open the project in Visual Studio Code.

Open the terminal:

```text
Terminal → New Terminal
```

Navigate to:

```bash
cd python-version
```

Run:

```bash
python main.py
```

---

## Web Version

Open:

```text
web-version/index.html
```

The application can be opened directly in a browser or served locally through a VS Code development server.

The Web Version uses:

```text
index.html
    +
style.css
    +
script.js
```

---

# Project Structure

The complete repository is organized as follows:

```text
company-attendance-system/
│
├── python-version/
│   │
│   ├── main.py
│   ├── database.py
│   ├── dashboard.py
│   ├── employees.py
│   ├── attendance.py
│   └── company_attnce.db
│
├── web-version/
│   │
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── LICENSE
└── README.md
```

This structure keeps the desktop and web implementations separated while allowing them to remain part of the same project.

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

If neither command works, Python may need to be installed or added to the system PATH.

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

## Employee Cannot Clock In

If an employee cannot clock in, check:

1. The employee has been registered.
2. The Employee ID is correct.
3. The employee does not already have an active attendance session.
4. The database is available.

---

## Employee Cannot Clock Out

If an employee cannot clock out, check:

1. The Employee ID is correct.
2. The employee has an active clock-in session.
3. The employee has not already clocked out.

---

## Attendance Information Is Missing

Make sure the Python application is using the correct SQLite database:

```text
company_attnce.db
```

The database stores the employee and attendance information used by the Python application.

---

## Web Version Is Not Displaying Correctly

Make sure the three files are inside the same folder:

```text
web-version/
├── index.html
├── style.css
└── script.js
```

Check that `index.html` correctly references:

```html
<link rel="stylesheet" href="style.css">
```

and:

```html
<script src="script.js"></script>
```

Also make sure the browser console does not show JavaScript errors.

---

# Future Improvements

The current system provides the core functionality of an employee attendance application. Future versions can expand the system further.

## Attendance

Possible improvements:

* Automatic working-hours calculation improvements
* Late arrival detection
* Early departure detection
* Overtime calculation
* Break tracking
* Absence tracking
* Attendance status
* Daily summaries
* Weekly summaries
* Monthly summaries

## Employee Management

Possible improvements:

* Employee profile pictures
* Departments
* Job positions
* Contact information
* Employee search
* Employee filtering
* Employee status

## Reports

Possible improvements:

* CSV export
* Excel export
* PDF reports
* Monthly attendance reports
* Individual employee reports
* Payroll-ready reports

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
* Deployment to a web server

## Interface Improvements

Possible improvements:

* Improved animations
* Page transitions
* Interactive notifications
* Confirmation dialogs
* Improved statistics
* Responsive layouts
* Dark/light themes
* Mobile support

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
* Object-oriented programming
* Event-driven programming
* Date and time manipulation
* Input validation
* Error handling
* Data persistence
* Modular application design
* Responsive interface design
* Git and GitHub project organization

---

# Project Status

**Current Status: Expanded Python Desktop Version + Functional Web Version**

The project currently contains two implementations of the Company Attendance System.

## Python Version

A modular desktop-based application using:

```text
Python
CustomTkinter
SQLite
datetime
```

The Python version now includes:

```text
Dashboard
    │
    ├── Live Date and Time
    ├── Attendance Statistics
    ├── Attendance Summary
    ├── Quick Attendance
    ├── Currently Working Employees
    └── Today's Attendance
             │
             ▼
Employees
    │
    ├── Add Employee
    ├── Search Employee
    ├── Show All
    ├── Delete Employee
    ├── Clear Form
    └── Employee Validation
             │
             ▼
Attendance
    │
    ├── Clock In
    ├── Clock Out
    ├── Working Hours
    ├── Search Attendance
    ├── Today
    ├── Show All
    ├── Refresh
    └── Attendance Status
```

## Web Version

A browser-based application using:

```text
HTML
CSS
JavaScript
Local Storage
```

Both versions implement the core employee attendance workflow.

---

# Purpose

The purpose of this project is to create a practical employee attendance system while applying programming and software development concepts.

Instead of creating separate small programming exercises, this project combines multiple concepts into a single functional application.

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
