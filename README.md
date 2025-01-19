# 2024Final
Program Structure Overview

This project is a Student Management System built for managing student, instructor, and course data. The system features an admin login, student login, and instructor login, as well as the ability to manage students, instructors, and courses as an admin.
Executable File

    main.py
        Main entry point of the program. This file contains the logic for:
            Admin login authentication and management (add/view students, instructors, courses).
            Student login functionality.
            Instructor login functionality.
            Viewing and managing students, instructors, and courses.
            The entire program runs from this file.
            Features:
                Admin can log in, add students, instructors, and courses, and view all students, instructors, and courses.
                Students and instructors can log in and access their respective functionalities.

Utility Files

    utils.py
        This utility file contains helper functions used across the program:
            read_csv(): Reads data from a specified CSV file.
            validate_login(): Validates login credentials by comparing them with the data in the CSV files.

CSV Data Files

    admin.csv: Stores admin credentials (username, password).
    student.csv: Stores student data (first name, last name, username, password).
    instructor.csv: Stores instructor data (first name, last name, username, password, title).
    courses.csv: Stores course data (course number, course title, instructor username).
    enrollment.csv (optional): Can store student enrollments in courses (if used in future updates).

Notes for Viewers

    Running the Program: To use the system, start by running main.py. This file contains all of the functionalities needed for login and managing the data.
    Login:
        Admin login: Admin credentials are stored in admin.csv. Admins can manage students, instructors, and courses.
        Student login: Students can log in using their credentials from student.csv.
        Instructor login: Instructors can log in using their credentials from instructor.csv.
        (See csv files for usernames and passwords to interact with the program fully.)
    Features:
        Admin: Can log in, add/view students, instructors, and courses.
        Students: Can log in to view their details (future functionality can include more features).
        Instructors: Can log in to view their courses (future functionality can include more features).
    Ensure that all CSV files (admin.csv, student.csv, instructor.csv, courses.csv, enrollment.csv) are present in the same directory as the Python files to ensure proper functionality.
