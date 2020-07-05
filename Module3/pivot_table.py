# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 23:59:17 2020

@author: shari
"""
import pandas as pd
import numpy as np

#Suppose we have a DataFrame with price and ratings for different bikes, 
#broken down by manufacturer and type of bicycle.

#Create a pivot table that shows the mean price and mean rating for 
#every 'Manufacturer' / 'Bike Type' combination.

#data sets
#   Bike Type Manufacturer  Price  Rating
#0   Mountain            A    400       8
#1   Mountain            A    600       9
#2       Road            A    400       4
#3       Road            A    450       4
#4   Mountain            B    300       6
#5   Mountain            B    250       5
#6       Road            B    400       4
#7       Road            B    500       6
#8   Mountain            C    400       5
#9   Mountain            C    500       6
#10      Road            C    800       9
#11      Road            C    950      10

#answer
#print(pd.pivot_table(Bikes, index=['Manufacturer','Bike Type']))
#                        Price  Rating
#Manufacturer Bike Type               
#A            Mountain   500.0     8.5
#             Road       425.0     4.0
#B            Mountain   275.0     5.5
#             Road       450.0     5.0
#C            Mountain   450.0     5.5
#             Road       875.0     9.5

df = pd.read_csv('cars.csv')
print(df.head())
print(df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean))
df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean,np.min], margins=True)
