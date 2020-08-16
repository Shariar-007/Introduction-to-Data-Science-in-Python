# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:29:38 2020

@author: shari
"""

import pandas as pd
import numpy as np

df = pd.read_csv('census.csv')

df = df[df['SUMLEV']==50]
#print(df)
#
#print(df['STNAME'].unique())
#
#inefficient
#for state in df['STNAME'].unique():
#    avg = np.average(df.where(df['STNAME'] == state).dropna()['CENSUS2010POP'])
#    print('Counties in the state '+ state + ' have an average population of ' + str(avg))
#    
#efficient
#for group, frame in df.groupby('STNAME'):
#    avg = np.average(frame['CENSUS2010POP'])
#    print('Countries in the state '+ group + ' have an average population of ' + str(avg))
#     
#print(df.head())

#df = df.set_index('STNAME')
#
#def fun(item):
#    if item[0]<'M':
#        return 0;
#    if item[0]<'Q':
#        return 1;
#    return 2;
#
#for group, frame in df.groupby(fun):
#    print('There are ' + str(len(frame)) + ' records in group '+ str(group) + ' for processing.')
#    


#df1 = pd.read_csv('shoppingdata.csv')
#Looking at our backpacking equipment DataFrame, suppose we are interested in 
#finding our total weight for each category. Use groupby to group the dataframe, 
#and apply a function to calculate the total weight (Weight x Quantity) by category.
    
#print(df1.groupby('Category').apply(lambda df1,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity'))

# Or alternatively without using a lambda:
#def totalweight(df, w, q):
#        return sum(df[w] * df[q])
#        
#print(df.groupby('Category').apply(totalweight, 'Weight (oz.)', 'Quantity'))

 

   
print(df.groupby('STNAME').agg({'CENSUS2010POP': np.average}))    

print(type(df.groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']))
print(type(df.groupby(level=0)['POPESTIMATE2010']))    
    
print((df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average, 'sum': np.sum})))    
    
#print(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011'].agg({'avg': np.average, 'sum': np.sum}))
    
    
#print(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011'].agg({'POPESTIMATE2010': np.average, 'POPESTIMATE2011': np.sum}))
    
    
# df.groupby(level=0)
# =============================================================================
#It specifies the first index of the Dataframe. When you have multiple indices 
#and you need to groupby only one index of those multiple indices of the dataframe
# we use it.
#
#It means:
#level 0 -> First Index
#level 1 -> Second Index    
# =============================================================================
    
#agg()    
# =============================================================================
# Pandas is one of those packages and makes importing and analyzing data much easier. 
# Pandas Series. agg() is used to pass a function or list of function to be applied on 
# a series or even each element of series separately. In case of list of function, 
# multiple results are returned by agg() method.


#Python is a great language for doing data analysis, primarily because of the fantastic
# ecosystem of data-centric Python packages. Pandas is one of those packages and makes
# importing and analyzing data much easier.
#
#Dataframe.aggregate() function is used to apply some aggregation across one or more 
#column. Aggregate using callable, string, dict, or list of string/callables. 
#Most frequently used aggregations are:
#
#sum: Return the sum of the values for the requested axis
#min: Return the minimum of the values for the requested axis
#max: Return the maximum of the values for the requested axis

#Syntax: DataFrame.aggregate(func, axis=0, *args, **kwargs)
#
#Parameters:
#func : callable, string, dictionary, or list of string/callables. Function to use 
#for aggregating the data. If a function, must either work when passed a DataFrame or 
#when passed to DataFrame.apply. For a DataFrame, can pass a dict, if the keys are 
#DataFrame column names.
#
#axis : (default 0) {0 or ‘index’, 1 or ‘columns’} 0 or ‘index’: apply function to 
#each column. 1 or ‘columns’: apply function to each row
# =============================================================================
    
    
    
    
    
    