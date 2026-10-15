from student import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    view_profile
)

from login import admin_login, student_login
from marks import add_marks, view_result,student_result

def main():

    while True:
        print("\n================================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Admin Login")
        print("2. Student Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            if admin_login():
                admin_menu()

        elif choice == "2":

            student = student_login()

            if student:
                student_menu(student)

        elif choice == "3":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


def admin_menu():

    while True:
        print("\n================================")
        print("          ADMIN MENU")
        print("================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Add Marks")
        print("7. View Student Result")
        print("8. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            add_marks()

        elif choice == "7":
            view_result()

        elif choice == "8":
            print("Admin logged out.")
            break

        else:
            print("Invalid choice. Please try again.")



def student_menu(student):

    while True:
        print("\n================================")
        print("        STUDENT MENU")
        print("================================")
        print("1. View My Profile")
        print("2. View My Result")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_profile(student)

        elif choice == "2":
            student_result(student[0])

        elif choice == "3":
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()