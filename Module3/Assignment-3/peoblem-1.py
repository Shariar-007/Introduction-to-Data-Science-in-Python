# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 22:33:41 2020

@author: shari
"""
import pandas as pd
import numpy as np

# =============================================================================
# # 1st way
# =============================================================================

#df = pd.ExcelFile('Energy Indicators.xls')
#energy = df.parse(skiprows=17,skip_footer=(38))
#energy = energy[['Unnamed: 1','Petajoules','Gigajoules','%']]
#energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
#energy['Energy Supply'] = 1000000*energy['Energy Supply']
#energy['Country'] = energy['Country'].replace({'Republic of Korea':'South Korea','United States of America':'United States','United Kingdom of Great Britain and Northern Ireland':'United Kingdom','United States of America':'United States','China, Hong Kong Special Administrative Region':'Hong Kong'})
##to remove numbers and/or parenthesis in their name
#energy['Country'] = energy['Country'].str.replace(r"\s+\(.*\)","")
#
#
#
#GDP = pd.read_csv('world_bank.csv',skiprows=4)
#GDP['Country Name']=GDP['Country Name'].replace({'Korea, Rep.':'South Korea','Iran, Islamic Rep.':'Iran','Hong Kong SAR, China':'Hong Kong'})
#GDP = GDP[['Country Name','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']]
#GDP.columns = ['Country','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
#
#
#ScimEn = pd.read_excel(io='scimagojr-3.xlsx')
#ScimEn = ScimEn[:15]
#
#df1 = pd.merge(ScimEn,energy, how='inner', left_on='Country', right_on='Country')
#final_df = pd.merge(df1,GDP, how='inner', left_on='Country', right_on='Country')
#final_df = final_df.set_index('Country')
#print(final_df.size)


# =============================================================================
# 2nd way
# =============================================================================

#energy = pd.read_excel('Energy Indicators.xls', skipfooter=38, skiprows=17, usecols='C:F')
#energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
#energy.loc[energy['Energy Supply'] == '...'] = np.NaN
#energy[['Energy Supply', 'Energy Supply per Capita']] = energy[['Energy Supply', 'Energy Supply per Capita']].apply(pd.to_numeric)
#energy['Energy Supply'] = energy['Energy Supply']*10**6
#energy['Country'] = energy['Country'].str.replace(r" \(.*\)","")
#energy['Country'] = energy['Country'].str.replace(r"([0-9]+)$","")
#replace_dict={"Republic of Korea": "South Korea",
#                  "United States of America": "United States",
#                  "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
#                  "China, Hong Kong Special Administrative Region": "Hong Kong"}
#energy['Country'].replace(to_replace=replace_dict, inplace=True)
#energy.reset_index()
#energy = energy.set_index('Country')
#
#GDP = pd.read_csv('world_bank.csv', skiprows=4)
#replace_dict = {"Korea, Rep.": "South Korea", 
#                "Iran, Islamic Rep.": "Iran",
#                "Hong Kong SAR, China": "Hong Kong"}
#GDP['Country Name'].replace(to_replace=replace_dict, inplace=True)
#years_to_keep = np.arange(2006, 2016).astype(str)
#GDP = GDP[np.append(['Country Name'],years_to_keep)]
##GDP.reset_index()
#GDP = GDP.rename(columns={'Country Name': 'Country'})
##GDP = GDP.set_index('GDP')
#
#ScimEn = pd.read_excel('scimagojr-3.xlsx', header=0)
#ScimEn.reset_index()
#ScimEn = ScimEn.set_index('Country')


#first_merge = pd.merge(energy, GDP, how='outer', left_index=True, right_index=True)
#result = pd.merge(ScimEn, first_merge, how='outer', left_index=True, right_index=True)
#
#result = result.reset_index().dropna(thresh=result.shape[1]-10).set_index('Country')
#result = result.loc[result['Rank']<=15]
    
#print(result.shape)
#print(energy.head)

# =============================================================================
# way 3
# =============================================================================

    
energy = pd.read_excel("Energy Indicators.xls",skip_footer=38,skip_header=1,skiprows=17) # Skip header and footer
# Skippped head and footer

energy.drop(energy.columns[[0,1]],axis=1,inplace=True) 
# Dropped first 2 columns

energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']

energy['Energy Supply'] *= 1000000 
# Converted to gigajoules

energy.dropna() 
# Drop rows with NaNs

energy['Country'] = energy['Country'].str.replace(r'\(.*\)', '') 
# Removee parenthesis

energy['Country'] = energy['Country'].str.replace('\d+', '')
# Removed numbers from names
  
energy['Country'] = energy['Country'].str.strip()

# So Iran's energy values back by deleting the spaces left from removal of parenthesis
 

for col in energy:
    energy[col] = energy[col].replace('...',np.nan)
# Any blank values will convert to NaN

energy['Country'] = energy['Country'].str.replace('Republic of Korea','South Korea')
energy['Country'] = energy['Country'].str.replace('United States of America','United States')
energy['Country'] = energy['Country'].str.replace('United Kingdom of Great Britain and Northern Ireland','United Kingdom')
energy['Country'] = energy['Country'].str.replace('China, Hong Kong Special Administrative Region','Hong Kong')
# Updating country names

GDP = pd.read_csv('world_bank.csv', skiprows=3) 
# Skipped header

new_header = GDP.iloc[0]
GDP = GDP[1:]
GDP.columns = new_header
# First row is now column names


GDP['Country Name'] = GDP['Country Name'].str.replace('Korea, Rep.','South Korea')
GDP['Country Name'] = GDP['Country Name'].str.replace('Iran, Islamic Rep.','Iran')
GDP['Country Name'] = GDP['Country Name'].str.replace('Hong Kong SAR, China','Hong Kong')
# Updating country names


names = GDP.columns.tolist()
names[names.index('Country Name')] = 'Country'
GDP.columns = names
# Change column from "Country Name" to "Country

GDP = GDP.drop(GDP.iloc[:,1:50], axis=1)
# Keeping columns from 2006-15 and dropping column number 1 to 50 

GDP.columns = GDP.columns.astype(str).str.split('.').str[0] 
# Removed '.0' at the end of the year columns    

  

ScimEn = pd.read_excel('scimagojr-3.xlsx')

Newdf = pd.merge(ScimEn,energy,how='outer',left_on='Country',right_on='Country')
Newdf2 = pd.merge(Newdf,GDP,how='outer',left_on='Country',right_on='Country')

Newdf2 = Newdf2[:15] 
# Top 15 countries

Newdf3 = Newdf2.set_index('Country') 
# Setting 'Country' for the index column

print(Newdf3)




















