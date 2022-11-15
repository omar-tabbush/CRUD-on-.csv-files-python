import studentController
import CourseController
import StudentCourseController
import entities
import charts
import pandas as pd
import numpy as np
import matplotlib as matl


dfStudent = pd.read_csv('./dataset/students.csv')
dfCourse = pd.read_csv('./dataset/courses.csv')
dfRel = pd.read_csv('./dataset/1student -to- many courses.csv')

while True:

    print("\n\n")
    print("'1'. enter student menu...")
    print("'2'. enter courses menu...")
    print("'3'. enter Registration menu...")
    print("'4'. enter grades menu...")
    print("'5'. enter charts menu...")
    print("'6'. Exit program")
    cmd = input()
    if (cmd == '1'):

        print("\n\n")
        print("'1'. add student:")
        print("'2'. delete student:")
        print("'3'. update student:")
        print("'4'. list all students:")
        print("'5'. list student by id:")
        print("'6'. exit student menu")
        sudcmd = input()
        if (sudcmd == '1'):
            studentController.add(entities.Student(
                name=input("enter student name: ")), df=dfStudent)
            continue
        elif (sudcmd == '2'):
            studentController.deleteById(
                input("enter student id: "), df=dfStudent, filename="students")
            continue
        elif (sudcmd == '3'):
            studentController.updateById(input("enter student id: "), entities.Student(
                name=input("enter student name: ")), df=dfStudent, filename="students")
            continue
        elif (sudcmd == '4'):
            studentController.printAll(df=dfStudent)
            continue
        elif (sudcmd == '5'):
            studentController.printById(
                input("enter student id: "), df=dfStudent)
            continue
        elif (sudcmd == '6'):
            break
        else:
            print("wrong input")
    elif (cmd == '2'):

        print("\n\n")
        print("'1'. add course:")
        print("'2'. delete course:")
        print("'3'. update course:")
        print("'4'. list all courses:")
        print("'5'. list course by id:")
        print("'6'. exit courses menu")
        crscmd = input()
        if (crscmd == '1'):
            CourseController.add(entities.Course(
                name=input("enter course name: "), code=input("enter course code: ")), df=dfCourse)
            continue
        elif (crscmd == '2'):
            CourseController.deleteById(
                input("enter course id: "), df=dfCourse, filename="courses")
            continue
        elif (crscmd == '3'):
            CourseController.updateById(input("enter course id: "), entities.Course(
                name=input("enter course name: ")), df=dfCourse, filename="courses")
            continue
        elif (crscmd == '4'):
            CourseController.printAll(df=dfCourse)
            continue

        elif (crscmd == '5'):
            CourseController.printById(
                input("enter course id: "), df=dfCourse)
            continue

        elif (crscmd == '6'):
            continue
        else:
            print("??")
    elif (cmd == '3'):
        print("'1'. Show the registered courses for a student")
        print("'2'. Show the registered student for a course")
        print("'3'. Add courses for students")
        print("'4'. Drop courses for students")
        print("'5'. exit Registration menu")
        regcmd = input()
        if (regcmd == '1'):
            StudentCourseController.getCoursesInStudent(studId=input(
                "enter student id: "), dfRel=dfRel, dfCourse=dfCourse)
            continue
        elif (regcmd == '2'):
            StudentCourseController.getStudentsInCourse(courseId=input(
                "enter course id: "), dfRel=dfRel, dfStudent=dfStudent)
            continue
        elif (regcmd == '3'):
            StudentCourseController.add(entities.StudentCourse(
                studentId=input("enter student id: "),
                courseId=input("enter course id: ")
            ))
            continue
        elif (regcmd == '4'):
            StudentCourseController.deleteById(
                input("enter student id: "), df=dfRel, )
            continue
        elif (regcmd == '5'):
            continue
        else:
            print("??")
    elif (cmd == '4'):
        print("'1'. add grade to a student:")
        print("'2'. delete grade to a student:")
        print("'3'. update grade to a student for one course:")
        print("'4'. list all grades to a student for all courses:")
        print("'5'. list grade to a student for a course:")
        print("'6'. exit grades menu")
        gradecmd = input()
        if (gradecmd == '1'):
            StudentCourseController.updateGradeBy_studIdOrCourseId(input("enter student id: "), entities.StudentCourse(
                grade=input("enter grade: ")), dfRel=dfRel,)
            continue
        elif (gradecmd == '2'):
            StudentCourseController.deleteGradeBy_studIdOrCourseId(
                input("enter student id: "), dfRel=dfRel, )
            continue
        elif (gradecmd == '3'):
            StudentCourseController.updateGradeBy_studIdOrCourseId(input("enter student id: "), entities.StudentCourse(
                grade=input("enter grade: ")), dfRel=dfRel, )
            continue
        elif (gradecmd == '4'):
            StudentCourseController.getGrades(
                input("enter student id: "), dfRel=dfRel)
            continue
        elif (gradecmd == '5'):
            StudentCourseController.getGrade(
                input("enter student id: "), input("enter course id: "), dfRel=dfRel)
            continue
        elif (gradecmd == '6'):
            continue
        else:
            print("wrong input")

    elif (cmd == '5'):
        print("1. grades of a student:")
        print("2. Passed/Failed/AW students:")
        print("3. average of each course:")
        print("4. number of students for each course:")
        print("5. exit grades menu")
        chartcmd = input()
        if (chartcmd == '1'):
            charts.charts_gradesofstudent()
            continue
        elif (chartcmd == '2'):
            charts.charts_gradesofcourse()
            continue
        elif (chartcmd == '3'):
            charts.charts_averageOfCourses()
            continue
        elif (chartcmd == '4'):
            charts.charts_nbOfStudentsInCourses()
            continue
        elif (gradecmd == '5'):
            continue
        else:
            print("wrong input")
    elif (cmd == '6'):
        print("bye bye")
        break
    else:
        print("wrong input")
        continue
