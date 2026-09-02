# Clock In / Clock Out System

A Python-based employee attendance management system that allows employees to clock in and clock out while keeping track of attendance records. The application uses a graphical user interface built with CustomTkinter and stores data using SQLite.

## Description

The Clock In / Clock Out System is a desktop application designed to simplify employee attendance tracking.

Employees can be added to the system and their attendance can be recorded by using the Clock In and Clock Out functions. The system automatically records the date and time of each attendance action and stores the information in an SQLite database.

The application is organized into separate modules for employee management, attendance tracking, database operations, and the dashboard.

## Features

### Dashboard
- Displays the main system interface
- Provides access to employee and attendance functions
- Provides an overview of the attendance system

### Employee Management
- Add employee records
- View employee information
- Manage employee records
- Assign employee IDs

### Clock In
- Records an employee's clock-in time
- Automatically records the current date
- Prevents duplicate clock-ins when an employee is already clocked in

### Clock Out
- Records an employee's clock-out time
- Automatically records the current date and time
- Completes the employee's attendance record

### Attendance Tracking
- Stores employee attendance records
- Records clock-in and clock-out times
- Keeps attendance history
- Allows attendance information to be viewed through the application

### Database
- Uses SQLite for data storage
- Automatically stores employee information
- Stores attendance records
- Keeps data available after closing the application

## Technologies Used

- **Python** – Main programming language
- **CustomTkinter** – Graphical User Interface
- **SQLite** – Database management
- **Datetime** – Date and time handling

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
