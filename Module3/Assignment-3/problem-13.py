# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 02:47:54 2020

@author: shari
"""

import pandas as pd
import numpy as np
import matplotlib as plt

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

############################################################################
def plot_optional():
    Top15 = final_df
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);
    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')
    print("This is an example of a visualization that can be created to help understand the data. \
This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
2014 GDP, and the color corresponds to the continent.")
print(plot_optional())