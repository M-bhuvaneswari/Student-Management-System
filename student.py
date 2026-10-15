#================= Add new Student ====================#

def add_student():
    print("\n--- Add Student ---")

    student_id= int(input("Enter Student Id :"))
    name= input("Enter Student Name :")
    age= int(input("Enter Student Age :"))
    department = input("Enter Department :")
    email= input("Enter Email Id : ")
    password = input("Create Password: ")

    student= f"{student_id},{name},{age},{department},{email},{password}\n"

    with open("data/students.txt", "a") as file:
        file.write(student)

#add_student()
    print("Student added successfully!")

#================= Search all Students =================#

def view_students():
    print("\n------- Student List ---------")

    try:
        with open("data/students.txt","r") as f1:
            students= f1.readlines()

            if not students:
                print("No Students found!")
                return
            for student in students:
                data= student.strip().split(",")

                print("Student ID :",data[0])
                print("Student Name :",data[1])
                print("Student Age :",data[2])
                print("Student Department :",data[3])
                print("Email ID :",data[4])
                print("-----------------------------")

    except FileNotFoundError:
        print("Student file not found.")
#view_students()


#=================== Search Student ====================#

def search_student():
    print("\n--- Search Student ---")

    search_id = input("Enter Student ID: ")

    try:
        with open("data/students.txt", "r") as file:
            for student in file:
                data = student.strip().split(",")

                if data[0] == search_id:
                    print("\nStudent Found!")
                    print("Student ID :", data[0])
                    print("Name       :", data[1])
                    print("Age        :", data[2])
                    print("Department :", data[3])
                    print("Email      :", data[4])
                    return

            print("Student not found.")

    except FileNotFoundError:
        print("Student file not found.")

#search_student()

#=================== Update Student =====================#

def update_student():
    print("\n--- Update Student ---")

    search_id = input("Enter Student ID to update: ")

    try:
        with open("data/students.txt", "r") as file:
            students = file.readlines()

        found = False

        for i in range(len(students)):
            data = students[i].strip().split(",")

            if data[0] == search_id:
                print("\nStudent found!")
                print("Enter new details:")

                name = input("Enter Name: ")
                age = input("Enter Age: ")
                department = input("Enter Department: ")
                email = input("Enter Email: ")

                students[i] = f"{search_id},{name},{age},{department},{email}\n"

                found = True
                break

        if found:
            with open("data/students.txt", "w") as file:
                file.writelines(students)

            print("Student updated successfully!")

        else:
            print("Student not found.")

    except FileNotFoundError:
        print("Student file not found.")


#update_student()

#=================== Delete Student ======================#

def delete_student():
    print("\n--- Delete Student ---")

    search_id = input("Enter Student ID to delete: ")

    try:
        with open("data/students.txt", "r") as file:
            students = file.readlines()

        found = False
        updated_students = []

        for student in students:
            data = student.strip().split(",")

            if data[0] == search_id:
                found = True
            else:
                updated_students.append(student)

        if found:
            with open("data/students.txt", "w") as file:
                file.writelines(updated_students)

            print("Student deleted successfully!")

        else:
            print("Student not found.")

    except FileNotFoundError:
        print("Student file not found.")

#delete_student()

def view_profile(student):
    print("\n--- My Profile ---")
    print("Student ID :", student[0])
    print("Name       :", student[1])
    print("Age        :", student[2])
    print("Department :", student[3])
    print("Email      :", student[4])
