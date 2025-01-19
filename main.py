from admin_module import admin_menu
from student_module import student_menu
from instructor_module import instructor_menu

def main():
    while True:
        print("\nWelcome to the School Management System")
        print("1. Admin Login")
        print("2. Student Login")
        print("3. Instructor Login")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            admin_menu()
        elif choice == '2':
            student_menu()
        elif choice == '3':
            instructor_menu()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
