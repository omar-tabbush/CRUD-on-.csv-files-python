import pandas as pd
import matplotlib.pyplot as matl
import numpy as np
import entities
import StudentCourseController as scc
matl.style.use('ggplot')

dfStudent = pd.read_csv('./dataset/students.csv')
dfCourse = pd.read_csv('./dataset/courses.csv')
dfRel = pd.read_csv('./dataset/1student -to- many courses.csv')


def charts_gradesofstudent(studId, dfRel, dfCourse):
    x = scc.getCoursesInStudent(studId, dfCourse, dfRel)
    x1 = [dfCourse.iloc[a].to_string(index=False) for a in x]
    print("_____________________________")
    print(x1)
    print("_____________________________")
    y = scc.getGrades(studId=studId, dfRel=dfRel)['grade'].values.tolist()
    print(y)
    matl.bar(x1, y,)
    matl.show()


def charts_gradesofcourse(courseId, dfRel, dfStudent):
    x = scc.getStudentsInCourse(courseId, dfStudent, dfRel)
    print(x)
    x1 = [dfStudent.iloc[a].to_string(index=False) for a in x]
    print("_____________________________")
    print(x1)
    print("_____________________________")
    y = []
    for a in x:
        y.insert(-1, scc.getGrade(studId=a, courseId=courseId,
                 dfRel=dfRel).to_string(index=False))

    print(y)
    matl.bar(x1, y,)
    matl.show()


def charts_averageOfCourses(dfCourse, dfRel):
    gradesinCourse = []
    # print(list(dfCourse.index))
    for courseId in list(dfCourse.index):
        gradesinCourse.insert(-1, dfRel[dfRel['courseId']
                              == courseId]['grade'].mean())
    print(gradesinCourse)
    matl.bar(dfCourse['courseName'].values.tolist(), gradesinCourse,)
    matl.show()


def charts_nbOfStudentsInCourses(dfCourse, dfRel):
    nbOfStudentsInCourses = []
    # print(list(dfCourse.index))
    for courseId in list(dfCourse.index):
        nbOfStudentsInCourses.insert(-1,
                                     dfRel[dfRel['courseId'] == courseId]['grade'].count())
    print(nbOfStudentsInCourses)
    matl.bar(dfCourse['courseName'].values.tolist(), nbOfStudentsInCourses,)
    matl.show()
