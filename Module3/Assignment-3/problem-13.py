# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 02:47:54 2020

@author: shari
"""

import pandas as pd
import numpy as np

# =============================================================================
# code of problem-1 for problem 3
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
# solution of problem-8
# =============================================================================

# =============================================================================
# way - 1
# =============================================================================
def answer_thirteen():
    Top15 = final_df
    Top15['PopEst'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15['PopEst'] = Top15['PopEst'].apply('{:,}'.format)
    return Top15['PopEst'] 
print (answer_thirteen())


# =============================================================================
# way - 2
# =============================================================================
def answer_thirteen():
    Top15 = final_df
    Top15['PopEst'] = (Top15.iloc[:,7]/Top15.iloc[:,8]).astype(float)
    return Top15['PopEst']
print (answer_thirteen())

# =============================================================================
# way - 3
# =============================================================================

def answer_thirteen():
    Top15 = final_df
    Top15['PopEst'] = (Top15['Energy Supply']/Top15['Energy Supply per Capita'])
    return Top15['PopEst'].apply(lambda x: '{0:,}'.format(x)).astype(str)
    # Adds in comma separators.
print (answer_thirteen())