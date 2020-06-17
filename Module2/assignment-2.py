# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 00:24:35 2020

@author: shari
"""

import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

print(df.head())

names_ids = df.index.str.split('\s\(') # split the index by '('
print(names_ids)

df.index = names_ids.str[0]
df['ID'] = names_ids.str[1].str[:3]

df = df.drop('Totals')
print(df.head())

def answer_zero():
    return df.iloc[0]

print(answer_zero())

print("Q1. Which country has won the most gold medals in summer games?")
def answer_one():
#    df[df['Gold'] == df['Gold'].max()]['ID']
    return df[df['Gold'] == df['Gold'].max()].index

print(answer_one())

#print(df.index)
print("Q2. Which country had the biggest difference between their summer and winter gold medal counts?")

def answer_two():
    return  df[(df['Total'] - df['Total.1']) ==(df['Total'] - df['Total.1']).max()].index

print(answer_two())

print("Q3. Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count?")
#solution = (summer gold - winter gold)/Total Gold

def answer_three():
    return (((df[(df['Gold']-df['Gold.1'])/df['Combined total'] == ((df['Gold']-df['Gold.1'])/df['Combined total']).max()])['Gold'] >= 1) & ((df[(df['Gold']-df['Gold.1'])/df['Combined total'] == ((df['Gold']-df['Gold.1'])/df['Combined total']).max()])['Gold.1'] >= 1)).index

#def answer_three():
#    return (df[(df['Gold'] >= 1) & (df['Gold.1'] >= 1)])

print(answer_three())

print("Q4. Write a function that creates a Series called 'Point' which is a weighted value where each gold medal (Gold.2) counts for 3 points, silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2) for 1 point. The function should return only the column (a Series object) which you created, with the country names as indices.")
def answer_four():
    df['Points'] = df['Gold.2']*3 + df['Silver.2']*2 + df['Bronze.2']*1
    return df['Points']

print(answer_four())


# =============================================================================
# Part 2
# =============================================================================
census_df = pd.read_csv('census.csv')
print(census_df.head())

print("Q5.Which state has the most counties in it?")
def answer_five():
    return census_df[census_df['COUNTY'] == census_df['COUNTY'].max()]['STNAME']
print(answer_five())

print("Q6.Which state has the most counties in it?")
def answer_six():
    return census_df.sort_values('CENSUS2010POP',ascending = False).head(3).STNAME
print(answer_six())

print("Q7. Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)")
def answer_seven():
    return census_df[((census_df[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].max(axis=1)) -  (census_df[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].min(axis=1)).abs()) == ((census_df[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].max(axis=1)) -  (census_df[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].min(axis=1)).abs()).max()].STNAME
print(answer_seven())

print("Q8.")
def answer_eight():
    return census_df[((census_df['REGION'] == 1) | (census_df['REGION'] == 2)) & (census_df['POPESTIMATE2015'] > census_df['POPESTIMATE2014']) & (census_df['CTYNAME'].str.startswith('Washington'))][['STNAME','CTYNAME']]
print(answer_eight())















