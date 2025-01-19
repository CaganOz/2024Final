import csv
from utils import read_csv, validate_login

ADMINS_FILE = 'admin.csv'
STUDENTS_FILE = 'student.csv'
INSTRUCTORS_FILE = 'instructor.csv'
COURSES_FILE = 'courses.csv'
ENROLLMENTS_FILE = 'enrollment.csv'

def admin_login():
    """Authenticate the admin with username and password."""
    print("Admin Login")
    for attempt in range(5):
        username = input("Enter admin username: ").strip()
        password = input("Enter admin password: ").strip()
        if validate_login(username, password, ADMINS_FILE):
            print("Login successful!")
            return True
        else:
            print(f"Incorrect username or password. Attempts remaining: {4 - attempt}")
    print("Too many incorrect attempts. Exiting.")
    return False


def add_student():
    """Add a new student to the system."""
    students = read_csv(STUDENTS_FILE)
    usernames = {student['username'] for student in students}

    print("Add a New Student")
    while True:
        first_name = input("Enter First Name: ").strip()
        last_name = input("Enter Last Name: ").strip()
        username = input("Enter Unique Username: ").strip()
        password = input("Enter Password: ").strip()

        if username in usernames:
            print(f"Username '{username}' is already taken. Please choose another.")
            continue

        new_student = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'password': password
        }
        students.append(new_student)
        usernames.add(username)

        with open(STUDENTS_FILE, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['first_name', 'last_name', 'username', 'password'])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(new_student)

        print(f"Student '{username}' added successfully.")
        another = input("Would you like to add another student? (yes/no): ").strip().lower()
        if another != 'yes':
            break


def add_instructor():
    """Add a new instructor to the system."""
    instructors = read_csv(INSTRUCTORS_FILE)
    usernames = {instructor['username'] for instructor in instructors}

    print("Add a New Instructor")
    while True:
        first_name = input("Enter First Name: ").strip()
        last_name = input("Enter Last Name: ").strip()
        username = input("Enter Unique Username: ").strip()
        password = input("Enter Password: ").strip()
        title = input("Enter Title (Assistant Professor/Associate Professor/Professor): ").strip()

        if username in usernames:
            print(f"Username '{username}' is already taken. Please choose another.")
            continue

        if title not in ["Assistant Professor", "Associate Professor", "Professor"]:
            print("Invalid title. Please enter one of the specified titles.")
            continue

        new_instructor = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'password': password,
            'title': title
        }
        instructors.append(new_instructor)
        usernames.add(username)

        with open(INSTRUCTORS_FILE, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['first_name', 'last_name', 'username', 'password', 'title'])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(new_instructor)

        print(f"Instructor '{username}' added successfully.")
        another = input("Would you like to add another instructor? (yes/no): ").strip().lower()
        if another != 'yes':
            break


def add_course():
    """Add a new course to the system."""
    courses = read_csv(COURSES_FILE)
    instructors = read_csv(INSTRUCTORS_FILE)
    course_numbers = {course['course_number'] for course in courses}
    instructor_usernames = {instructor['username'] for instructor in instructors}

    print("Add a New Course")
    while True:
        course_number = input("Enter Unique Course Number: ").strip()
        course_title = input("Enter Course Title: ").strip()
        instructor_username = input("Enter Instructor Username: ").strip()

        if course_number in course_numbers:
            print(f"Course number '{course_number}' is already taken. Please choose another.")
            continue

        if instructor_username not in instructor_usernames:
            print(f"Instructor username '{instructor_username}' not found. Please try again.")
            continue

        new_course = {
            'course_number': course_number,
            'course_title': course_title,
            'instructor_username': instructor_username
        }
        courses.append(new_course)
        course_numbers.add(course_number)

        with open(COURSES_FILE, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['course_number', 'course_title', 'instructor_username'])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(new_course)

        print(f"Course '{course_number}' added successfully.")
        another = input("Would you like to add another course? (yes/no): ").strip().lower()
        if another != 'yes':
            break


def view_all_students():
    """View all student information."""
    students = read_csv(STUDENTS_FILE)
    if not students:
        print("No students found.")
        return
    print("\nAll Students:")
    print(f"{'First Name':<15}{'Last Name':<15}{'Username':<15}{'Password':<15}")
    for student in students:
        print(f"{student['first_name']:<15}{student['last_name']:<15}{student['username']:<15}{student['password']:<15}")


def view_all_instructors():
    """View all instructor information."""
    instructors = read_csv(INSTRUCTORS_FILE)
    if not instructors:
        print("No instructors found.")
        return
    print("\nAll Instructors:")
    print(f"{'First Name':<15}{'Last Name':<15}{'Username':<15}{'Password':<15}{'Title':<20}")
    for instructor in instructors:
        print(f"{instructor['first_name']:<15}{instructor['last_name']:<15}{instructor['username']:<15}{instructor['password']:<15}{instructor['title']:<20}")


def view_all_courses():
    """View all course information."""
    courses = read_csv(COURSES_FILE)
    if not courses:
        print("No courses found.")
        return
    print("\nAll Courses:")
    print(f"{'Course Number':<15}{'Course Title':<30}{'Instructor Username':<20}")
    for course in courses:
        print(f"{course['course_number']:<15}{course['course_title']:<30}{course['instructor_username']:<20}")


def admin_menu():
    """Main menu for admin functionality."""
    if admin_login():
        while True:
            print("\nAdmin Menu")
            print("1. Add Student")
            print("2. Add Instructor")
            print("3. Add Course")
            print("4. View All Students")
            print("5. View All Instructors")
            print("6. View All Courses")
            print("7. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                add_student()
            elif choice == '2':
                add_instructor()
            elif choice == '3':
                add_course()
            elif choice == '4':
                view_all_students()
            elif choice == '5':
                view_all_instructors()
            elif choice == '6':
                view_all_courses()
            elif choice == '7':
                print("Exiting Admin Menu.")
                break
            else:
                print("Invalid option. Try again.")
