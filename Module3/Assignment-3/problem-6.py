# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 01:35:16 2020

@author: shari
"""
import pandas as pd
import numpy as np

# =============================================================================
# code of problem-1 for problem 6
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
# solution of problem-6
# =============================================================================

# =============================================================================
# way - 1
# =============================================================================

result = final_df['% Renewable'].idxmax()
print(result, final_df.loc[result, '% Renewable'])

# =============================================================================
# way - 2
# =============================================================================

ans = final_df[final_df['% Renewable'] == max(final_df['% Renewable'])]
print(ans.index.tolist()[0],ans['% Renewable'].tolist()[0])

# =============================================================================
# way - 3
# =============================================================================

mx = final_df.iloc[:,9].max()
print('Brazil',mx)

# =============================================================================
# way - 4
# =============================================================================

maxRenewable = final_df['% Renewable'].idxmax(), final_df['% Renewable'].max()
print('Brazil',mx)
