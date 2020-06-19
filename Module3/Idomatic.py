# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 22:08:50 2020

@author: shari
"""
import pandas as pd
df = pd.read_csv('census.csv')

print(df.head())

print(df.where(df['SUMLEV'] == 50).dropna().set_index(['STNAME','CTYNAME']).rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))

df1 = df[df['SUMLEV']==50] 
print(df1.head())

df1.set_index(['STNAME','CTYNAME'], inplace=True)
print(df1.head())

df1.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})
print(df1.head())

#show column name
print(df1.columns.values.tolist())

import numpy as np

def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({'min': np.min(data), 'max': np.max(data)})
print(df.apply(min_max, axis=1))


def min_max1(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    row['max'] = np.max(data)
    row['min'] = np.min(data)
    return row
print(df.apply(min_max1, axis=1))


rows = ['POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015']
print(df.apply(lambda x: np.max(x[rows]), axis=1))






