# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:00:36 2020

@author: shari
"""
import pandas as pd
df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
                   {'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
                   {'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
                  index=['Store 1', 'Store 1', 'Store 2'])
#print(df)

df['Date'] = ['December 1', 'January 1', 'mid-May']
#print(df)

df['Delivered'] = True
#print(df)

df['Feedback'] = ['Positive', None, 'Negative']
#print(df)

adf = df.reset_index()
#print(adf)

adf['Date'] = pd.Series({0: 'December 1', 2: 'mid-May'})
#print(adf)

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])

staff_df = staff_df.set_index('Name')
#print(staff_df.head())

student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])

student_df = student_df.set_index('Name')
#print(student_df.head())

#print(pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True))

#print(pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True))

#print(pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True))
#
#print(pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True))

staff_df = staff_df.reset_index()
student_df = student_df.reset_index()

#print(staff_df)
#print(student_df)
#print(pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name'))

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])

student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])

#print(pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name'))

staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])


#print(staff_df)
#print(student_df)
#
#print(pd.merge(staff_df, student_df, how='inner', left_on=['First Name','Last Name'], right_on=['First Name','Last Name']))
#


