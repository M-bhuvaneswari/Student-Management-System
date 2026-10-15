class Student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
        self.__grade = None

    def calculate_grade(self):
        if self.marks>=90:
            self.__grade= "A"
        elif self.marks>=75:
            self.__grade="B"
        elif self.marks>=60:
            self.__grade="C"
        else:
            self.__grade="D"

    def display_details(self):
        print(f"Name :{self.name}, Roll Number : {self.roll_number},Marks :{self.marks},Grade :{self.__grade}")


class Course:
    def __init__(self,course_name,code,credits):
        self.course_name=course_name
        self.code=code
        self.credits=credits


class Admin:
    def __init__(self):
        self.students=[]
    def add_student(self,student):
        self.students.append(student)

    def remove_student(self,roll_number):
        self.students=[s for s in self.students if s.roll_number!= roll_number]

    def display_all_students(self):
        for student in self.students:
            student.display_details()



class Report:
    def __init__(self,student):
        self.student= student

    def generate_transcript(self):
        print(f"Transcript for {self.student.name}")
        self.student.calculate_grade()
        self.student.display_details()

s1=Student("Alice",101,92)
s2=Student("Kala",102,88)
s3= Student("Jai",103,95)
s4=Student("Karthik",104,90)
s5=Student("Neha",105,97)

s1.calculate_grade()
s2.calculate_grade()
s3.calculate_grade()
s4.calculate_grade()
s5.calculate_grade()


admin=Admin()
admin.add_student(s1)
admin.add_student(s2)
admin.add_student(s3)
admin.add_student(s4)
admin.add_student(s5)
admin.display_all_students()

report= Report(s1)
report.generate_transcript()


    

