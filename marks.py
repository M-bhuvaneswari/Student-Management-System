def add_marks():
    print("\n--- Add Marks ---")

    student_id = input("Enter Student ID: ")

    python = int(input("Enter Python mark: "))
    sql = int(input("Enter SQL mark: "))
    maths = int(input("Enter Maths mark: "))
    english = int(input("Enter English mark: "))

    marks = f"{student_id},{python},{sql},{maths},{english}\n"

    with open("data/marks.txt", "a") as file:
        file.write(marks)

    print("Marks added successfully!")

def view_result():
    print("\n--- Student Result ---")

    student_id = input("Enter Student ID: ")

    try:
        with open("data/marks.txt", "r") as file:

            for record in file:
                data = record.strip().split(",")

                if data[0] == student_id:

                    python = int(data[1])
                    sql = int(data[2])
                    maths = int(data[3])
                    english = int(data[4])

                    total = python + sql + maths + english
                    average = total / 4

                    if average >= 90:
                        grade = "A+"
                    elif average >= 80:
                        grade = "A"
                    elif average >= 70:
                        grade = "B"
                    elif average >= 60:
                        grade = "C"
                    elif average >= 50:
                        grade = "D"
                    else:
                        grade = "F"

                    print("\nPython  :", python)
                    print("SQL     :", sql)
                    print("Maths   :", maths)
                    print("English :", english)
                    print("-------------------")
                    print("Total   :", total)
                    print("Average :", average)
                    print("Grade   :", grade)

                    if average >= 50:
                        print("Result  : PASS")
                    else:
                        print("Result  : FAIL")

                    return

            print("Marks not found.")

    except FileNotFoundError:
        print("Marks file not found.")

#add_marks()
#iew_result()


def student_result(student_id):
    print("\n--- My Result ---")

    try:
        with open("data/marks.txt", "r") as file:

            for record in file:
                data = record.strip().split(",")

                if data[0] == student_id:

                    python = int(data[1])
                    sql = int(data[2])
                    maths = int(data[3])
                    english = int(data[4])

                    total = python + sql + maths + english
                    average = total / 4

                    if average >= 90:
                        grade = "A+"
                    elif average >= 80:
                        grade = "A"
                    elif average >= 70:
                        grade = "B"
                    elif average >= 60:
                        grade = "C"
                    elif average >= 50:
                        grade = "D"
                    else:
                        grade = "F"

                    print("\nPython  :", python)
                    print("SQL     :", sql)
                    print("Maths   :", maths)
                    print("English :", english)
                    print("-------------------")
                    print("Total   :", total)
                    print("Average :", average)
                    print("Grade   :", grade)

                    if average >= 50:
                        print("Result  : PASS")
                    else:
                        print("Result  : FAIL")

                    return

            print("Result not available.")

    except FileNotFoundError:
        print("Marks file not found.")