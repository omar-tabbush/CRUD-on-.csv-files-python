import pandas as pd
import matplotlib as matl
import numpy as np
import entities


def printAll(df):
    print(df)

# df = pd.read_csv('./dataset/courses.csv')
# printAll(df=df)


def printById(id, df):
    print(df.iloc[id])

# df = pd.read_csv('./dataset/courses.csv')
# printById(0,df=df)


def deleteById(id, df, filename):
    param = str(df.at[id, 'courseCode'])  # param for the relational file
    df.drop([id], axis=0, inplace=True)
    df.to_csv('./dataset/'+filename+'.csv', index=False, header=True)
    dfRel = pd.read_csv('./dataset/1student -to- many courses.csv')
    dfRel = dfRel[dfRel.courseCode != param]
    print(dfRel)


# df = pd.read_csv('./dataset/courses.csv')
# deleteById(7,df=df,filename='courses')
# print(df)

# print(df.at[0,'courseCode'])

def updateById(id, Course, df, filename):
    param = str(df.at[id, 'courseCode'])  # param for the relational file
    # df = pd.read_csv('./dataset/courses.csv')
    df.at[id, 'courseCode'] = Course.code
    df.at[id, 'courseName'] = Course.name
    df.to_csv('./dataset/'+filename+'.csv', index=False, header=True)
    dfRel = pd.read_csv('./dataset/1student -to- many courses.csv')
    # dfRel[dfRel.courseCode == param] =  Course.code
    dfRel['courseCode'].replace(
        to_replace=param, value=Course.code, inplace=True)
    dfRel.to_csv('./dataset/1student -to- many courses.csv',
                 index=False, header=True)


# df = pd.read_csv('./dataset/courses.csv')
# print(df)
# print("_______________To_____________________")
# mycourse = entities.Course('c2', 'hacking')
# print("---")
# updateById(id=0, df=df, filename='courses', Course=mycourse)
# print("---")
# print(df)


def add(Course,df):
    df.iloc[-1] = [Course.code,
                   Course.name]
    df.to_csv('./dataset/courses.csv', index=False, header=True)


# mycourse = entities.Course('c2', 'hacking')
# add(Course=mycourse)
