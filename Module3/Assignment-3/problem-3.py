# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 03:47:08 2020

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
print(final_df.size)


# =============================================================================
# solution of problem-3 
# =============================================================================

# =============================================================================
# way - 1
# =============================================================================
avgGDP = final_df[['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']].mean(axis=1).rename('avgGDP').sort_values(ascending=False)
#return pd.Series(avgGDP)
print(avgGDP)

# =============================================================================
# way - 2
# =============================================================================
years_to_keep = np.arange(2006, 2016).astype(str)
final_df['avgGDP'] = final_df[years_to_keep].mean(axis=1)
final_df['avgGDP'].sort_values(ascending=False)

print(final_df['avgGDP'])

# =============================================================================
# way-3
# =============================================================================

final_df = final_df.iloc[:,10:] 
# Only include the years for columns
avgGDP = final_df.mean(axis=1)
avgSDP = avgGDP.sort_values(ascending=False)
print(avgSDP)





