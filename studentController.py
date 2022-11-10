import pandas as pd
import matplotlib as matl
import numpy as np
import entities

df = pd.read_csv('./dataset/students.csv')
print(df)


def printAll(df):
    print(df)

def printById(id, df):
    print(df.iloc[id])


def deleteById(id, df, filename):
    param = str(id)  # param for the relational file
    df.drop([id], axis=0, inplace=True)
    df.to_csv('./dataset/'+filename+'.csv', index=False, header=True)
    dfRel = pd.read_csv('./dataset/1student -to- many courses.csv')
    dfRel = dfRel[dfRel.studID != param]
    dfRel.to_csv('./dataset/1student -to- many courses.csv',
                 index=False, header=True)


def updateById(id, Student,df,filename):
    df.at[id,'student']=Student.name
    df.to_csv('./dataset/'+filename+'.csv', index=False, header=True)
    

def add(Student):
    df.iloc[-1] = [Student.name]
    df.to_csv('./dataset/courses.csv', index=False, header=True)
