from utils import read_csv, validate_login

INSTRUCTORS_FILE = 'instructors.csv'
COURSES_FILE = 'courses.csv'
ENROLLMENTS_FILE = 'enrollments.csv'

def instructor_login():
    """Authenticate the instructor with username and password."""
    print("Instructor Login")
    for attempt in range(5):
        username = input("Enter instructor username: ").strip()
        password = input("Enter instructor password: ").strip()
        if validate_login(username, password, INSTRUCTORS_FILE):
            print("Login successful!")
            return username
        else:
            print(f"Incorrect username or password. Attempts remaining: {4 - attempt}")
    print("Too many incorrect attempts. Exiting.")
    return None

def view_assigned_courses(username):
    """View courses assigned to the instructor."""
    courses = read_csv(COURSES_FILE)
    assigned_courses = [course for course in courses if course['instructor_username'] == username]
    if not assigned_courses:
        print("No courses assigned to you.")
        return
    print("\nYour Courses:")
    print(f"{'Course Number':<15}{'Course Title':<30}")
    for course in assigned_courses:
        print(f"{course['course_number']:<15}{course['course_title']:<30}")

def view_enrollments(username):
    """View enrollments for courses assigned to the instructor."""
    courses = read_csv(COURSES_FILE)
    enrollments = read_csv(ENROLLMENTS_FILE)
    instructor_courses = {course['course_number'] for course in courses if course['instructor_username'] == username}
    
    print("\nEnrollments for Your Courses:")
    print(f"{'Course Number':<15}{'Student Username':<30}")
    for enrollment in enrollments:
        if enrollment['course_number'] in instructor_courses:
            print(f"{enrollment['course_number']:<15}{enrollment['username']:<30}")

def instructor_menu():
    """Main menu for instructor functionality."""
    username = instructor_login()
    if not username:
        return
    while True:
        print("\nInstructor Menu")
        print("1. View Assigned Courses")
        print("2. View Enrollments")
        print("3. Logout")
        choice = input("Choose an option: ")
        if choice == '1':
            view_assigned_courses(username)
        elif choice == '2':
            view_enrollments(username)
        elif choice == '3':
            print("Logging out. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
