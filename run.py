import studentController
import CourseController
import StudentCourseController
import entities
import pandas as pd
import numpy as np
import matplotlib as matl

print("\n\n")
print("1. enter student menu...")
print("2. enter courses menu...")
print("3. enter Registration menu...")
print("4. enter grades menu...")
print("5. Exit program")
dfStudent = pd.read_csv('./dataset/students.csv')
dfCourse = pd.read_csv('./dataset/courses.csv')
dfRel = pd.read_csv('./dataset/1student -to- many courses.csv')
while True:
    cmd = int(input())

    if (cmd == 1):
        print("\n\n")
        print("1. add student:")
        print("2. delete student:")
        print("3. update student:")
        print("4. list all students:")
        print("5. list student by id:")
        print("6. exit student menu")
        if (input() == 1):
            studentController.add(entities.Student(
                name=input("enter student name: ")))
        elif (input() == 2):
            studentController.deleteById(
                input("enter student id: "), studentController.df, "students")
        elif (input() == 3):
            studentController.updateById(input("enter student id: "), entities.Student(
                name=input("enter student name: ")), studentController.df, "students")
        elif (input() == 4):
            studentController.printAll(studentController.df)
        elif (input() == 5):
            studentController.printById(
                input("enter student id: "), studentController.df)
        elif (input() == 6):
            break
        else:
            print("wrong input")
    elif (cmd == 2):
        print("\n\n")
        print("1. add course:")
        print("2. delete course:")
        print("3. update course:")
        print("4. list all courses:")
        print("5. list course by id:")
        print("6. exit courses menu")
        if (input() == 1):
            CourseController.add(entities.Course(
                name=input("enter course name: ")))
        elif (input() == 2):
            CourseController.deleteById(
                input("enter course id: "), CourseController.df, "courses")
        elif (input() == 3):
            CourseController.updateById(input("enter course id: "), entities.Course(
                name=input("enter course name: ")), CourseController.df, "courses")

        elif (input() == 4):
            CourseController.printAll(CourseController.df)

        elif (input() == 5):
            CourseController.printById(
                input("enter course id: "), CourseController.df)

        elif (input() == 6):
            break
        else:
            print("??")
    elif (cmd == 3):
        print("1. Show the registered courses for a student")
        print("2. Show the registered student for a course")
        print("3. Add courses for students")
        print("4. Drop courses for students")
        print("5. exit Registration menu")
        if (input() == 1):
            StudentCourseController.printAll(StudentCourseController.df)
        elif (input() == 2):
            StudentCourseController.printAll(StudentCourseController.df)

        elif (input() == 3):
            StudentCourseController.add(entities.StudentCourse(
                studentId=input("enter student id: "),
                courseId=input("enter course id: ")
            ))
        elif (input() == 4):
            StudentCourseController.deleteById(
                input("enter student id: "), StudentCourseController.df, "studentcourses")
        elif (input() == 5):
            break
        else:
            print("??")
    elif (cmd == 4):
        print("1. add grade to a student:")
        print("2. delete grade to a student:")
        print("3. update grade to a student for one course:")
        print("4. list all grades to a student for all courses:")
        print("5. list grade to a student for a course:")
        print("6. exit grades menu")
        if (input() == 1):
            StudentCourseController.updateGradeBy_studIdOrCourseId(input("enter student id: "), entities.StudentCourse(
                grade=input("enter grade: ")), StudentCourseController.df, "studentcourses")
        elif (input() == 2):
            StudentCourseController.deleteGradeBy_studIdOrCourseId(
                input("enter student id: "), StudentCourseController.df, "studentcourses")
        elif (input() == 3):
            StudentCourseController.updateGradeBy_studIdOrCourseId(input("enter student id: "), entities.StudentCourse(
                grade=input("enter grade: ")), StudentCourseController.df, "studentcourses")
        elif (input() == 4):
            StudentCourseController.getGrades(
                input("enter student id: "), StudentCourseController.df)
        elif (input() == 5):
            StudentCourseController.getGrade(
                input("enter student id: "), input("enter course id: "))
        elif (input() == 6):
            break
        else:
            print("wrong input")

    elif (cmd == 5):
        print("bye bye")
        break
    else:
        print("wrong input")
        continue
