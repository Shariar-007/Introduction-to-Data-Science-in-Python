# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 01:53:04 2020

@author: shari
"""
import pandas as pd
import numpy as np

#s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])
#s.astype('category', categories=['Low', 'Medium', 'High'], ordered=True)
#print(s)
#
#
#s1 = pd.Series([168, 180, 174, 190, 170, 185, 179, 181, 175, 169, 182, 177, 180, 171])
#pd.cut(s1, 3)
##print(pd.cut(s1, 3))
#
### You can also add labels for the sizes [Small < Medium < Large].
#print(pd.cut(s1, 3, labels=['Small', 'Medium', 'Large']))


df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
df.rename(columns={0: 'Grades'}, inplace=True)
#print(df)
#print(df['Grades'].astype('category').head())

grades = df['Grades'].astype('category',
                             categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                             ordered=True)
#print(grades.head())

#print(grades > 'C')

df1 = pd.read_csv('census.csv')
df1 = df1[df1['SUMLEV']==50]
df1 = df1.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
print(df1.head())
df2 = pd.cut(df1['avg'],10)
print(df2)