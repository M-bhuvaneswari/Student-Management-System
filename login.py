import os


def admin_login():
    print("\n------- Admin Login --------")

    username = input("Enter Username :")
    password = input("Enter Password :")
    admin_password = os.environ.get("ADMIN_PASSWORD")

    if not admin_password:
        print("Admin login is not configured. Set the ADMIN_PASSWORD environment variable.")
        return False

    if username == "admin" and password == admin_password:
        print("Login Successful!!")
        return True

    print("Invalid Username and Password!!!")
    return False


def student_login():
    print("\n-------- Student Login ---------")

    student_id = input("Enter student Id :")
    password = input("Enter password :")

    try:
        with open("data/students.txt", "r") as file:
            for student in file:
                data = student.strip().split(",")

                if data[0] == student_id and data[5] == password:
                    print("\nLogin successful!")
                    print("Welcome", data[1])
                    return data

            print("Invalid Student ID or Password.")
            return None

    except FileNotFoundError:
        print("Student file not found.")
        return None


#student_login()
