import pandas as pd
import matplotlib as matl
import numpy as np
import entities

# df = pd.read_csv('./dataset/students.csv')
#TO DO:
#check if studId is valiable

# get courses registered by studId
def getCoursesInStudent(studId,df):
    dfRel = pd.read_csv('./dataset/1student -to- many courses.csv')
    aa = dfRel[dfRel['studId'] ==studId]['courseId'].values.tolist()
    # print(aa)
    for x in aa:
        print(df.iloc[x])


# get studId registered by courses
def getStudentsInCourse(courseId, df):
    dfRel = pd.read_csv('./dataset/1student -to- many courses.csv')
    aa = dfRel[dfRel['courseId'] == courseId]['studId'].values.tolist()
    # print(aa)
    for x in aa:
        print(df.iloc[x])
    

# remove course registered by studId
def deleteCourseInstudent(studId, df): 
    dfRel = pd.read_csv('./dataset/1student -to- many courses.csv')
    dfRel = dfRel[dfRel['studId'] != studId]
    dfRel.to_csv('./dataset/1student -to- many courses.csv',
                 index=False, header=True)


# get grades & courses by studId
def getGrades(studId):
    dfRel = pd.read_csv('./dataset/1student -to- many courses.csv')
    aa = dfRel[dfRel['studId'] == studId][[
        'courseId', 'grade']].values.tolist()
    tdf = pd.DataFrame(data={'course': [x[0] for x in aa], 'grade': [x[1] for x in aa]})
    print(tdf.to_string(index=False))

# get grade for studId for one courses 
def getGrade(studId,courseId):
    dfRel = pd.read_csv('./dataset/1student -to- many courses.csv')
    aa = dfRel[dfRel['studId'] == studId][[
        'courseId', 'grade']].values.tolist()
    aa = aa[aa['courseId'] == courseId]['grade']
    print(aa)


# update grade by studId & courseId
def updateGradeBy_studIdOrCourseId(studId, courseId):
    dfRel = pd.read_csv('./dataset/1student -to- many courses.csv')
    paramI = dfRel.index[(dfRel['studId'] == studId) & (
        dfRel['courseId'] == courseId)].values.tolist()
    print(paramI)
    dfRel.at[paramI[0], 'grade'] = 'D'
    dfRel.to_csv('./dataset/1student -to- many courses.csv',
                 index=False, header=True)


# delete grade by studId & courseId
def deleteGradeBy_studIdOrCourseId(studId, courseId):
    dfRel = pd.read_csv('./dataset/1student -to- many courses.csv')
    paramI = dfRel.index[(dfRel['studId'] == studId) & (
        dfRel['courseId'] == courseId)].values.tolist()
    print(paramI)
    dfRel.at[paramI[0], 'grade'] = np.nan
    dfRel.to_csv('./dataset/1student -to- many courses.csv',
                 index=False, header=True)
