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

The dashboard is designed to give users a quick overview of the current attendance system.

---

# Employee Management

The Employee Management section allows users to maintain employee information.

Features include:

* Add employees
* View employees
* Manage employee records
* Select employees for attendance
* Associate employees with attendance records
* Organize employee information

Employee information is connected to attendance records so that every clock-in and clock-out can be associated with the correct employee.

---

# Clock In

The Clock In feature records the beginning of an employee's work session.

When an employee clocks in, the system:

1. Identifies the selected employee.
2. Gets the current date.
3. Gets the current time.
4. Creates an attendance record.
5. Stores the clock-in information.
6. Associates the attendance record with the employee.

Example:

```text
Employee: Jose Navoa
Date: September 3, 2026
Clock In: 08:02 AM
Status: Currently Working
```

The system is designed to prevent unnecessary duplicate clock-ins for an employee who already has an active attendance session.

---

# Clock Out

The Clock Out feature records when an employee finishes their work session.

When an employee clocks out, the system:

1. Identifies the employee.
2. Finds the active attendance session.
3. Gets the current time.
4. Updates the attendance record.
5. Saves the clock-out information.

Example:

```text
Employee: Jose Navoa
Date: September 3, 2026
Clock In: 08:02 AM
Clock Out: 05:04 PM
Status: Completed
```

This creates a complete attendance session containing both the clock-in and clock-out times.

---

# Attendance Records

The Attendance section allows users to review recorded attendance.

An attendance record can contain:

* Employee ID
* Employee name
* Date
* Clock-in time
* Clock-out time
* Attendance status
* Work session information

Example:

| Employee   | Date       | Clock In | Clock Out | Status    |
| ---------- | ---------- | -------- | --------- | --------- |
| Jose Navoa | 2026-09-03 | 08:02 AM | 05:04 PM  | Completed |
| Employee 2 | 2026-09-03 | 08:15 AM | 05:10 PM  | Completed |

Attendance information is retained so previous records can be reviewed.

---

# Python Desktop Version

The Python version is a desktop application built using **Python and CustomTkinter**.

It provides a graphical interface that allows users to manage employees and attendance from a desktop environment.

## Technologies

* Python
* CustomTkinter
* SQLite
* `datetime`

## Python Features

The Python version includes:

* Desktop graphical interface
* Dashboard
* Employee management
* Clock In
* Clock Out
* Attendance records
* SQLite database
* Persistent data storage
* Input validation
* Attendance session management
* Modular Python structure

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
└── company_attendance.db
```

### `main.py`

The main entry point of the Python application.

Responsible for:

* Starting the application
* Initializing the GUI
* Loading application components
* Starting the main window

### `database.py`

Handles SQLite database operations.

Responsible for:

* Creating the database
* Creating tables
* Connecting to SQLite
* Storing employee information
* Storing attendance information
* Performing database operations

### `dashboard.py`

Contains the main dashboard interface.

Responsible for:

* Main application layout
* Navigation
* Dashboard information
* Connecting different sections

### `employees.py`

Handles employee management.

Responsible for:

* Adding employees
* Displaying employees
* Managing employee information
* Selecting employees

### `attendance.py`

Handles attendance functionality.

Responsible for:

* Clock In
* Clock Out
* Recording dates
* Recording times
* Displaying attendance records
* Managing attendance sessions

### `company_attendance.db`

The SQLite database used to store persistent application data.

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

No Python installation is required to open the basic Web Version.

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
| Clock In           | Yes             | Yes                   |
| Clock Out          | Yes             | Yes                   |
| Attendance Records | Yes             | Yes                   |
| Persistent Storage | SQLite          | Local Storage         |
| Installation       | Python required | Browser required      |
| Internet Required  | No              | No for local version  |

---

# Why Two Versions?

The project contains two versions to demonstrate how the same software concept can be developed using different technologies.

### Python Version

The Python version demonstrates:

* Python programming
* GUI development
* SQLite
* Object-oriented programming
* Database management
* CRUD operations
* Desktop application development

### Web Version

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
        Select Employee               Clock In
                                            │
                                            ▼
                                       Work Session
                                            │
                                            ▼
                                         Clock Out
                                            │
                                            ▼
                                    Attendance Record
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

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python        | Main programming language |
| CustomTkinter | Desktop GUI               |
| SQLite        | Database                  |
| datetime      | Date and time             |

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

### Functions

Used to organize operations such as:

* Adding employees
* Clocking in
* Clocking out
* Retrieving attendance
* Updating records

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
* Delete/manage records where supported

### Event-Driven Programming

Both versions respond to user actions such as:

* Clicking buttons
* Selecting employees
* Submitting forms
* Clocking in
* Clocking out

### Date and Time Handling

The system automatically records attendance dates and times.

### Data Persistence

The project demonstrates how application data can remain available after the application or webpage is closed.

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
│   └── company_attendance.db
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

## Web Version is not displaying correctly

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

* Automatic working-hours calculation
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

**Current Status: Functional Python Desktop Version + Functional Web Version**

The project currently contains two implementations of the Company Attendance System:

### Python Version

A desktop-based application using:

```text
Python
CustomTkinter
SQLite
```

### Web Version

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
