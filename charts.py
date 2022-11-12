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
    matl.bar(x1,y,)
    matl.show()

