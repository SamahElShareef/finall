"""
TODO 1 Enter your name and submission date
Name :'Samah EL Shareef'
Delivery Date :20/6
"""

# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark (user_input)
import uuid


class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark


course_id = input("Enter the course id: ")
course_name = input("Enter the course name: ")
course_mark = float(input("Enter the course mark: "))

course = Course(course_name, course_mark)


class Student:
    # TODO 3 define static variable indicates total student count
    total_students = 0

    # TODO 4 define a constructor which includes
    # student_id (unique using uuid module)
    # student_name (user input)
    # student_age (user input)
    # student_number (user_input)
    # courses_list (List of Course Objects)

    def __init__(self, student_name, student_age, student_number, courses_list):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = courses_list
        Student.total_students += 1
        pass


student_name = input("Enter the student name: ")
student_age = int(input("Enter the student age: "))
student_number = input("Enter the student number: ")
courses_list = []
student = Student(student_name, student_age, student_number, courses_list)


# TODO 5 define a method to enroll new course to student courses list
def enroll_course(self, course_name, course_mark):
    course = Course(course_name, course_mark)
    self.courses_list.append(course)


# method to get_student_details as dict
def get_student_details(self):
    return self._dict_


# method to get_student_courses


def get_student_courses(self):
    for course in self.courses_list:
        print("Course Name:", course.course_name)
        print("Course Mark:", course.course_mark)

    # TODO 6 print student courses with their marks
    pass


# method to get student_average as a value
def get_student_average(self):
    total_marks = sum(course.course_mark for course in self.courses_list)
    return total_marks / len(self.courses_list)

    # TODO 7 return the student average
    pass


# in Global Scope
# TODO 8 declare empty students list
students_list = []

while True:
    #try:

# TODO 9 handle Exception for selection input
    # ***************************************************************
    try:
     number = int(input("Enter any number from 1 to 6"))
    except ValueError:
        print("Invalid Input. Please enter a valid integer for the selection.")

    if 1 <= number <= 6:
        print("this number is valid")
    else:
        print("this number is not valid , pleas try another choice")

    selection = int(input("1.Add New Student\n"
                          "2.Delete Student\n"
                          "3.Display Student\n"
                          "4.Get Student Average\n"
                          "5.Add Course to student with mark.\n"
                          "6.Exit"))

    if selection == 1:

        # TODO 10 make sure that Student number is not exists before
        student_number = input("Enter Student Number")

        for student in students_list:
            if (student.student_number == student_number):
                print("Student Number already exists")
                student_number = input("Please inter a deffirent number")
            else:
                print("Student Added Successfully.")
        break

        student_name = input("Enter Student Name")

        # TODO 11 create student object and append it to students list
        student = Student(student_name, student_age, student_number)
        students_list.append(student)

        print("Student Added Successfully")
        # ******************************************************************

    elif selection == 2:
        student_number = input("Enter Student Number")
        # TODO 12 find the target student using loops and delete it if exist , if not print ("Student Not Exist")
        while True:
            for student in students_list:
                if student.student_number == student_number:
                    students_list.remove(found_student)
                    print("Student Deleted Successfully.")
                else:
                    print("Student Not Found.")
        break
        # ***********************************************************************



    elif selection == 3:
        student_number = input("Enter Student Number")
        # TODO 13 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")
        while True:
            for student in students_list:
                if student.student_number == student_number:
                    print(" The Student Details:")
                    print("Student ID:", found_student.student_id)
                    print("Student Name:", found_student.student_name)
                    print("Student Age:", found_student.student_age)
                    print("Student Number:", found_student.student_number)
                    print("Courses List:", [course.course_name for course in found_student.courses_list])
                else:
                    print("This Student is Not Found.")
        break

    # ******************************************************************
    elif selection == 4:
        student_number = input("Enter Student Number")
        # TODO 14 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")
        while True:
            for student in students_list:
                if student.student_number == student_number:
                    average = found_student.get_student_average()
                    print("Student Average:", average)
                else:
                    print("This Student is Not  exist")
        break
    # **************************************************************

    elif selection == 5:
        student_number = input("Enter Student Number")
# TODO 15 ask user to enter course name and course mark then create coures object then append it to target student courses
        for student in students_list:
            if student.student_number == student_number:
                course_name = input("Enter Course Name: ")
                course_mark = float(input("Enter Course Mark: "))
                student.student_number.enroll_course(course_name, course_mark)
                print("Course Enrolled Successfully.")
            else:
                print("Student Not Found.")

    # ***************************************************************
    elif selection == 6:
        print("Exiting Program...")
        break

    else:
        print("Invalid Selection. Please try again.")
    pass


#print("Invalid Input. Please enter a valid integer for the selection.")
# TODO 16 call a function to exit the program
