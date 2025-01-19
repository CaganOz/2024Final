import csv 
from utils import read_csv, validate_login

STUDENTS_FILE = 'students.csv'
ENROLLMENTS_FILE = 'enrollments.csv'
COURSES_FILE = 'courses.csv'

def student_login():
    """Authenticate the student with username and password."""
    print("Student Login")
    for attempt in range(5):
        username = input("Enter student username: ").strip()
        password = input("Enter student password: ").strip()
        if validate_login(username, password, STUDENTS_FILE):
            print("Login successful!")
            return username
        else:
            print(f"Incorrect username or password. Attempts remaining: {4 - attempt}")
    print("Too many incorrect attempts. Exiting.")
    return None

def view_courses():
    """View all available courses."""
    courses = read_csv(COURSES_FILE)
    if not courses:
        print("No courses available.")
        return
    print("\nAvailable Courses:")
    print(f"{'Course Number':<15}{'Course Title':<30}")
    for course in courses:
        print(f"{course['course_number']:<15}{course['course_title']:<30}")

def enroll_in_course(username):
    """Enroll the student in a course."""
    courses = read_csv(COURSES_FILE)
    enrollments = read_csv(ENROLLMENTS_FILE)
    
    print("\nEnroll in a Course")
    view_courses()
    
    course_number = input("Enter the course number you wish to enroll in: ").strip()
    if not any(course['course_number'] == course_number for course in courses):
        print(f"Course '{course_number}' not found.")
        return
    
    if any(enrollment['username'] == username and enrollment['course_number'] == course_number for enrollment in enrollments):
        print(f"You are already enrolled in course '{course_number}'.")
        return
    
    with open(ENROLLMENTS_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['username', 'course_number'])
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow({'username': username, 'course_number': course_number})
    
    print(f"Successfully enrolled in course '{course_number}'.")

def student_menu():
    """Main menu for student functionality."""
    username = student_login()
    if not username:
        return
    while True:
        print("\nStudent Menu")
        print("1. View Available Courses")
        print("2. Enroll in a Course")
        print("3. Logout")
        choice = input("Choose an option: ")
        if choice == '1':
            view_courses()
        elif choice == '2':
            enroll_in_course(username)
        elif choice == '3':
            print("Logging out. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
