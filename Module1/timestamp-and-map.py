# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:51:25 2020

@author: shari
"""
import datetime as dt
import time as tm

#time returns the current time in seconds since the Epoch. (January 1st, 1970)
print(tm.time())


#Convert the timestamp to datetime.
dtnow = dt.datetime.fromtimestamp(tm.time())
print("date time:")
print(dtnow)

print("year: ")
print(dtnow.year)
print("month: ")
print(dtnow.month)
print("day: ")
print(dtnow.day)
print("hour: ")
print(dtnow.hour)

#timedelta is a duration expressing the difference between two dates. 
delta = dt.timedelta(days = 100) #create a timedelta of 100ays
print(delta)


today = dt.date.today()
print(today)

#day before 100 days from today
print(today - delta)

