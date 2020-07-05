# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 01:09:51 2020

@author: shari
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Timestamp
print(pd.Timestamp('9/1/2016 10:05AM'))

#Period
print(pd.Period('1/2016'))
print(pd.Period('3/5/2016'))

#DatetimeIndex
t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
print(t1)
print(type(t1.index))

#PeriodIndex
t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'), pd.Period('2016-11')])
print(t2)
print(type(t2.index))

#Converting to Datetime

d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab'))
print(ts3)

ts3.index = pd.to_datetime(ts3.index)
print(ts3)

pd.to_datetime('4.7.12', dayfirst=True)
print(pd.to_datetime('4.7.12', dayfirst=True))

### Timedeltas
pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016')
print(pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016'))

pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H')
print(pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H'))

### Working with Dates in a Dataframe
dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
print(dates)

df1 = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(),
                  'Count 2': 120 + np.random.randint(-5, 10, 9)}, index=dates)
print(df1)

print(df1.index.weekday_name)
print(df1.diff())
print(df1.resample('M').mean())
print(df1['2017'])
print(df1['2016-12'])
print(df1['2016-12':])
print(df1.asfreq('W', method='ffill'))


#%matplotlib inline
df1.plot()












