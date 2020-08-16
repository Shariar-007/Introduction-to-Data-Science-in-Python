# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 01:53:04 2020

@author: shari
"""
import pandas as pd
import numpy as np

# =============================================================================
# DataFrame. astype() method is used to cast a pandas object to a specified dtype. 
# astype() function also provides the capability to convert any suitable existing 
# column to categorical type. DataFrame
# 
# Syntax: DataFrame.astype(dtype, copy=True, errors=’raise’, **kwargs)
# 
# Parameters:
# dtype : Use a numpy.dtype or Python type to cast entire pandas object to the same type.
#  Alternatively, use {col: dtype, …}, where col is a column label and dtype is a numpy
#  .dtype or Python type to cast one or more of the DataFrame’s columns to column-specific
#  types.
#  
# copy : Return a copy when copy=True (be very careful setting copy=False as changes to 
# values then may propagate to other pandas objects).
# =============================================================================

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
print(df['Grades'].astype('category'))

grades = df['Grades'].astype('category',
                             categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                             ordered=True)
print(grades.head())

print(grades > 'C')

# =============================================================================
# 
# Use cut when you need to segment and sort data values into bins. This function is also 
# useful for going from a continuous variable to a categorical variable. For example, cut
#  could convert ages to groups of age ranges. Supports binning into an equal number of
#  bins, or a pre-specified array of bins.

#The cut() function is useful when we have a large number of scalar data and we want to
# perform some statistical analysis on it.
#
#For example, let’s say we have an array of numbers between 1 and 20. We want to divide
# them into two bins of (1, 10] and (10, 20] and add labels such as “Lows” and “Highs”. 
#We can easily perform this using the pandas cut() function.
#
#Furthermore, we can perform functions on the elements of a specific bin and label 
#elements.
# =============================================================================
 

df1 = pd.read_csv('census.csv')
df1 = df1[df1['SUMLEV']==50]
df1 = df1.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
print(df1.head())
df2 = pd.cut(df1['avg'],10)
print(df2)


# =============================================================================
# #The cut() function sytax is:
# #
# #
# #cut(
# #    x,
# #    bins,
# #    right=True,
# #    labels=None,
# #    retbins=False,
# #    precision=3,
# #    include_lowest=False,
# #    duplicates="raise",
# #)
# #x is the input array to be binned. It must be one-dimensional.
# #bins defines the bin edges for the segmentation.
# #right indicates whether to include the rightmost edge or not, default value is True.
# #labels is used to specify the labels for the returned bins.
# #retbins specifies whether to return the bins or not.
# #precision specifies the precision at which to store and display the bins labels.
# #include_lowest specifies whether the first interval should be left-inclusive or not.
# #duplicates speicifies what to do if the bins edges are not unique, whether to raise ValueError or drop non-uniques.
# =============================================================================

#What is a pivot table used for?
#A pivot table is a data summarization tool that is used in the context of data
# processing. Pivot tables are used to summarize, sort, reorganize, group, count, 
# total or average data stored in a database. It allows its users to transform columns 
# into rows and rows into columns.