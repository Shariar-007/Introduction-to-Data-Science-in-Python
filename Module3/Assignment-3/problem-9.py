# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 02:12:20 2020

@author: shari
"""
import pandas as pd
import numpy as np
import matplotlib as plt

# =============================================================================
# code of problem-1 for problem 9
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
# solution of problem-9
# =============================================================================

# =============================================================================
# way - 1
# =============================================================================
Top15 = final_df
Top15['Population Estimate'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
Top15['Citable Documents per Capita'] = Top15['Citable documents']/Top15['Population Estimate']

   
Top15['Citable Documents per Capita'] = Top15['Citable Documents per Capita'].astype(float)
Top15['Energy Supply per Capita'] = Top15['Energy Supply per Capita'].astype(float)
# Converted to float

print(Top15['Citable Documents per Capita'].corr(Top15['Energy Supply per Capita']))

# =============================================================================
# way - 2
# =============================================================================
Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
Top15['Citable docs per Capita'] = (Top15['Citable documents'] / Top15['PopEst']).astype(float)
ans = Top15['Citable docs per Capita'].corr(Top15['Energy Supply per Capita'])
print(ans)

# =============================================================================
# way - 3
# =============================================================================
Top15['Pop'] = Top15.iloc[:,7]/Top15.iloc[:,8]
Top15['Citable docs per Capita'] = (Top15.iloc[:,2]/Top15['Pop']).astype(float)
print(Top15[['Citable docs per Capita','Energy Supply per Capita']].corr(method='pearson').iloc[0,1])

Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])
