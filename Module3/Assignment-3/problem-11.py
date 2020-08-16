# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 02:33:27 2020

@author: shari
"""


import pandas as pd
import numpy as np

# =============================================================================
# code of problem-1 for problem 11
# =============================================================================
df = pd.ExcelFile('Energy Indicators.xls')
energy = df.parse(skiprows=17,skip_footer=(38))
energy = energy[['Unnamed: 1','Petajoules','Gigajoules','%']]
energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
energy['Energy Supply'] = 1000000*energy['Energy Supply']
energy['Country'] = energy['Country'].replace({'Republic of Korea':'South Korea','United States of America':'United States','United Kingdom of Great Britain and Northern Ireland':'United Kingdom','United States of America':'United States','China, Hong Kong Special Administrative Region':'Hong Kong'})
#to remove numbers and/or parenthesis in their name
energy['Country'] = energy['Country'].str.replace(r"\s+\(.*\)","")



GDP = pd.read_csv('world_bank.csv',skiprows=4)
GDP['Country Name']=GDP['Country Name'].replace({'Korea, Rep.':'South Korea','Iran, Islamic Rep.':'Iran','Hong Kong SAR, China':'Hong Kong'})
GDP = GDP[['Country Name','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']]
GDP.columns = ['Country','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']


ScimEn = pd.read_excel(io='scimagojr-3.xlsx')
ScimEn = ScimEn[:15]

df1 = pd.merge(ScimEn,energy, how='inner', left_on='Country', right_on='Country')
final_df = pd.merge(df1,GDP, how='inner', left_on='Country', right_on='Country')
final_df = final_df.set_index('Country')
#print(final_df.size)#

# =============================================================================
# solution of problem-11
# =============================================================================

# =============================================================================
# way - 1
# =============================================================================
def answer_twelve():
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    Top15 = final_df
    Top15 = Top15.reset_index()
    Top15['Continent'] = [ContinentDict[country] for country in Top15['Country']]
    Top15['bins'] = pd.cut(Top15['% Renewable'],5)
    return Top15.groupby(['Continent','bins']).size()
print(answer_twelve())

# =============================================================================
# way - 2
# =============================================================================
def answer_twelve():
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    Top15 = final_df
    Top15['Continent'] = None
    for i in range(len(Top15)):
        Top15.iloc[i,20]= ContinentDict[Top15.index[i]]
    Top15['bins'] = pd.cut(Top15['% Renewable'],5)
    return Top15.groupby(['Continent','bins']).size()

print(answer_twelve())

# =============================================================================
# way - 3
# =============================================================================
def answer_twelve():
    Top15 = final_df
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    
    # Map the dictionary values with the index values.
    Top15['Continent'] = Top15.index.to_series().map(ContinentDict)
    
    Top15['Bins'] = pd.cut(Top15['% Renewable'],5) # The ENTIRE range of % Renewable is split into 5 bins.
    
    return Top15.groupby(['Continent','Bins']).size() # The entire range of bins is then grouped by continent.

print(answer_twelve())