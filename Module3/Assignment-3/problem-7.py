# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 01:58:08 2020

@author: shari
"""

import pandas as pd
import numpy as np

# =============================================================================
# code of problem-1
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
# solution of problem-7
# =============================================================================

# =============================================================================
# way - 1
# =============================================================================
final_df['Citation Ratio'] = final_df['Self-citations']/final_df['Citations']
ans = final_df[final_df['Citation Ratio'] == max(final_df['Citation Ratio'])]
print (ans.index.tolist()[0],ans['Citation Ratio'].tolist()[0])


# =============================================================================
# way - 2
# =============================================================================

final_df['Ratio'] = final_df.iloc[:,4]/final_df.iloc[:,3]
print ('China',final_df.iloc[:,20].max())

# =============================================================================
# way - 3
# =============================================================================

final_df['Citation ratio'] = final_df['Self-citations'] / final_df['Citations']
MaxCitationRatio = final_df['Citation ratio'].idxmax(), final_df['Citation ratio'].max()
print (MaxCitationRatio)




