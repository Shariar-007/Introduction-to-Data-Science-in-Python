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
#    df[df['Gold'] == df['Gold'].max()].index
    return df[df['Gold'] == df['Gold'].max()].index[0]
print(answer_one())

#print(df.index)
print("Q2. Which country had the biggest difference between their summer and winter gold medal counts?")

def answer_two():
    return  df[(df['Gold'] - df['Gold.1']) ==(df['Gold'] - df['Gold.1']).max()].index[0]

print(answer_two())

print("Q2. Anothery way")
def answer_two_anotherway():
    df['gold_diff'] = (df['Gold'] - df['Gold.1']).abs()
    return df[(df['gold_diff']) ==(df['gold_diff']).max()].index[0]
print(answer_two_anotherway())

print("Q3. Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count?")
#solution = (summer gold - winter gold)/Total Gold
#def answer_three():
#    a = df[(df['Gold.1'] > 0) & (df['Gold'] > 0)].copy()
#    return a[((a['gold_diff'])/(a['Gold.2']) == ((a['gold_diff'])/(a['Gold.2'])).max())].index[0]

def answer_three():
    sub_df = df[(df['Gold'] > 0) & (df['Gold.1'] > 0)].copy()
    sub_df['rel'] = sub_df['gold_diff'] / sub_df['Gold.2']
    return sub_df[sub_df['rel'] == max(sub_df['rel'])].index[0]
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
#print(census_df.head())

print("Q5.Which state has the most counties in it?")
def answer_five():
#    census_df[census_df['COUNTY'] == census_df['COUNTY'].max()]['STNAME'].to_string(index=False)
    return census_df.groupby('STNAME')['COUNTY'].count().idxmax(axis = 0)
print(answer_five())


print("Q6.Which state has the most counties in it?")
def answer_six():
#    census_df.sort_values('CENSUS2010POP',ascending = False).head(3)['STNAME'].to_string(index=False)
    data = census_df[census_df['SUMLEV'] == 50].copy()
    return data.sort_values('CENSUS2010POP',ascending = False).head(3)['STNAME'].values.tolist()
print(answer_six())


print("Q7. Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)")

def answer_seven():
    data = census_df[census_df['SUMLEV'] == 50].copy()
    data['min_popestimate'] = data[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].min(axis=1)
    data['max_popestimate'] = data[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].max(axis=1)
    data['diff_popestimate'] = data['max_popestimate'] - data['min_popestimate']
    return data[data['diff_popestimate'] == data['diff_popestimate'].max()]['CTYNAME'].to_string(index=False)
print(answer_seven())

print("Q8.")
def answer_eight():
    return census_df[((census_df['REGION'] == 1) | (census_df['REGION'] == 2)) & (census_df['POPESTIMATE2015'] > census_df['POPESTIMATE2014']) & (census_df['CTYNAME'].str.startswith('Washington'))][['STNAME','CTYNAME']].sort_index(0)
print(answer_eight())















