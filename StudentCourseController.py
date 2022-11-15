import pandas as pd
import matplotlib as matl
import numpy as np
import entities

# df = pd.read_csv('./dataset/students.csv')
# TO DO:
# check if studId is valiable

# get courses registered by studId


def getCoursesInStudent(studId, dfCourse, dfRel):
    aa = dfRel[dfRel['studId'] == studId]['courseId'].values.tolist()
    if (aa):
        for x in aa:
            print(dfCourse.iloc[x])
    else:
        print('No courses registered')
    return (aa)


# get studId registered by courses
def getStudentsInCourse(courseId, dfStudent, dfRel):
    aa = dfRel[dfRel['courseId'] == courseId]['studId'].values.tolist()
    # print(aa)
    if (aa):
        for x in aa:
            print(dfStudent.iloc[x])
            return[]
    # else:
    #     print('No students registered')
    return (aa)


# remove course registered by studId
def deleteCourseInstudent(studId, dfRel):
    dfRel = dfRel[dfRel['studId'] != studId]
    dfRel.to_csv('./dataset/1student -to- many courses.csv',
                 index=False, header=True)


# get grades & courses by studId
def getGrades(studId, dfRel):
    aa = dfRel[dfRel['studId'] == studId][[
        'courseId', 'grade']].values.tolist()
    tdf = pd.DataFrame(data={'course': [x[0]
                       for x in aa], 'grade': [x[1] for x in aa]})
    print(tdf.to_string(index=False))
    return (tdf)

# get grade for studId for one course


def getGrade(studId, courseId, dfRel):
    aa = dfRel[dfRel['studId'] == studId][[
        'courseId', 'grade']]
    aa = aa[aa['courseId'] == courseId]['grade']
    print(aa)
    return (aa)

# update grade by studId & courseId
def updateGradeBy_studIdOrCourseId(studId, courseId, dfRel,Userinput):
    paramI = dfRel.index[(dfRel['studId'] == studId) & (
        dfRel['courseId'] == courseId)].values.tolist()
    print(paramI)
    dfRel.at[paramI[0], 'grade'] = Userinput
    dfRel.to_csv('./dataset/1student -to- many courses.csv',
                 index=False, header=True)


# delete grade by studId & courseId
def deleteGradeBy_studIdOrCourseId(studId, courseId, dfRel):
    paramI = dfRel.index[(dfRel['studId'] == studId) & (
        dfRel['courseId'] == courseId)].values.tolist()
    print(paramI)
    dfRel.at[paramI[0], 'grade'] = np.nan
    dfRel.to_csv('./dataset/1student -to- many courses.csv',
                 index=False, header=True)
