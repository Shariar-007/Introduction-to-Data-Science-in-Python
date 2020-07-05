# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:29:38 2020

@author: shari
"""

import pandas as pd
import numpy as np

df = pd.read_csv('census.csv')

df = df[df['SUMLEV']==50]
print(df)

print(df['STNAME'].unique())
#
#inefficient
for state in df['STNAME'].unique():
    avg = np.average(df.where(df['STNAME'] == state).dropna()['CENSUS2010POP'])
    print('Counties in the state '+ state + ' have an average population of ' + str(avg))
    
#efficient
for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])
    print('Countries in the state '+ group + ' have an average population of ' + str(avg))
     
#print(df.head())

df = df.set_index('STNAME')

def fun(item):
    if item[0]<'M':
        return 0;
    if item[0]<'Q':
        return 1;
    return 2;

for group, frame in df.groupby(fun):
    print('There are ' + str(len(frame)) + ' records in group '+ str(group) + ' for processing.')
    


#df1 = pd.read_csv('shoppingdata.csv')
#Looking at our backpacking equipment DataFrame, suppose we are interested in 
#finding our total weight for each category. Use groupby to group the dataframe, 
#and apply a function to calculate the total weight (Weight x Quantity) by category.
#print(df1.groupby('Category').apply(lambda df1,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity'))

# Or alternatively without using a lambda:
def totalweight(df, w, q):
        return sum(df[w] * df[q])
        
print(df.groupby('Category').apply(totalweight, 'Weight (oz.)', 'Quantity'))

 

   
print(df.groupby('STNAME').agg({'CENSUS2010POP': np.average}))    

print(type(df.groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']))
print(type(df.groupby(level=0)['POPESTIMATE2010']))    
    
print((df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average, 'sum': np.sum})))    
    
print(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011'].agg({'avg': np.average, 'sum': np.sum}))
    
    
print(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011'].agg({'POPESTIMATE2010': np.average, 'POPESTIMATE2011': np.sum}))
    
    
    
    
    
    
    
    
    
    
    
    