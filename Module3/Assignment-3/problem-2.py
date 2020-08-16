# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 01:21:03 2020

@author: shari
"""

import pandas as pd
import numpy as np

energy = pd.read_excel("Energy Indicators.xls",skipfooter=38,skip_header=1,skiprows=17) # Skip header and footer

energy.drop(energy.columns[[0,1]],axis=1,inplace=True) # Drop first 2 columns

energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']

energy.dropna() # Drop rows with NaN values.

energy['Country'] = energy['Country'].str.replace(r'\(.*\)', '') # Remove contents within parenthesis.
energy['Country'] = energy['Country'].str.replace('\d+', '') # Remove digits from names

#The str. strip() function is used to remove leading and trailing characters. 
#Strip whitespaces (including newlines) or a set of specified characters from 
#each string in the Series/Index from left and right sides
energy['Country'] = energy['Country'].str.strip() # This brings the Iran energy values back!


# Turn blank values into NaN
for col in energy:
    energy[col] = energy[col].replace('...',np.nan)

energy['Country'] = energy['Country'].str.replace('Republic of Korea','South Korea')
energy['Country'] = energy['Country'].str.replace('United States of America','United States')
energy['Country'] = energy['Country'].str.replace('United Kingdom of Great Britain and Northern Ireland','United Kingdom')
energy['Country'] = energy['Country'].str.replace('China, Hong Kong Special Administrative Region','Hong Kong')
#
#
## GDP:
#
GDP = pd.read_csv('world_bank.csv', skiprows=3) # Skip header
#
## Make first row the column names
new_header = GDP.iloc[0]
GDP = GDP[1:]
GDP.columns = new_header
#
#GDP = GDP.rename(index=str,columns = {"Country Name":"Country"})
#
GDP['Country Name'] = GDP['Country Name'].str.replace('Korea, Rep.','South Korea')
GDP['Country Name'] = GDP['Country Name'].str.replace('Iran, Islamic Rep.','Iran')
GDP['Country Name'] = GDP['Country Name'].str.replace('Hong Kong SAR, China','Hong Kong')
#
## Change column name from 'Country Name' to 'Country' for merging 3 files on country name.
names = GDP.columns.tolist()
names[names.index('Country Name')] = 'Country'
GDP.columns = names
#
## Only keep the columns from 2006-15. Drop column number 1 to 50. Don't need country code, etc.
GDP = GDP.drop(GDP.iloc[:,1:50], axis=1)
#
GDP.columns = GDP.columns.astype(str).str.split('.').str[0] # Remove '.0' at the end of the year columns.    


# SCIMEN:
ScimEn = pd.read_excel('scimagojr-3.xlsx')

# LOST ENTRIES = LEN(OUTER JOIN) - LEN(INNER JOIN)

# Need unique entries in all 3 sets so use concat. Can't do that with a left or right outer join!
value_outer = len(pd.concat([ScimEn['Country'],energy['Country'],GDP['Country']]).unique())
#
value_inter = (GDP.merge(energy, left_on='Country', right_on='Country', how='inner').merge(ScimEn, left_on='Country', right_on='Country', how='inner').shape[0])
#
#value_outer-value_inter
print(value_outer-value_inter)