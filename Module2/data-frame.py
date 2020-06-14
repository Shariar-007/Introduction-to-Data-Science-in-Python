# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 02:09:49 2020

@author: shari
"""
# =============================================================================
# The DataFrame Data Structure
# =============================================================================
import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})

purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})

purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

print(df)
print(df.loc['Store 2'])
print(type(df.loc['Store 2']))
print(df.loc['Store 1'])
print(df.loc['Store 1', 'Cost'])
print(df.T)
print(df.T.loc['Cost'])
print(df['Cost'])
print(df.loc['Store 1']['Cost'])
print(df.loc[:,['Name', 'Cost']])

df.drop('Store 1')
print(df)

copy_df = df.copy()
copy_df = copy_df.drop('Store 1') #row delete
print(copy_df)

del copy_df['Name'] #column delete
print(copy_df)

df['Location'] = None  #add an extra column
print(df)

# =============================================================================
# Dataframe Indexing and Loading
# =============================================================================
costs = df['Cost']
print(costs)

costs+=2
print(costs)

print(df)

df = pd.read_csv('olympics.csv')
print(df.head())

df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1)
print(df.head())

print(df.columns)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True) 
                           
print(df.head())

# =============================================================================
# Querying a DataFrame
# =============================================================================

print(df['Gold'] > 0)
only_gold = df.where(df['Gold'] > 0)
print(only_gold.head())

print(only_gold['Gold'].count())
print(df['Gold'].count())
#print(df.count())

only_gold = only_gold.dropna()
print(only_gold.head())

only_gold = df[df['Gold'] > 0]
print(only_gold.head())

print(len(df[(df['Gold'] > 0) | (df['Gold.1'] > 0)]))

print(df[(df['Gold.1'] > 0) & (df['Gold'] == 0)])
print(len(df[(df['Gold.1'] > 0) & (df['Gold'] == 0)]))