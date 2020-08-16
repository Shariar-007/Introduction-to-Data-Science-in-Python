# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 01:41:36 2020

@author: shari
"""

import pandas as pd
import numpy as np

def answer_one():
    df = pd.ExcelFile('Energy Indicators.xls')
    energy = df.parse(skiprows=17,skip_footer=(38))
    #when we read the xls file it become 6 column file but we make it 4 but mentioning, and exclude NaN
    #column
    energy = energy[['Unnamed: 1','Petajoules','Gigajoules','%']]  
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']] =  energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']].replace('...',np.NaN).apply(pd.to_numeric)
    energy['Energy Supply'] = 1000000*energy['Energy Supply']
    energy['Country'] = energy['Country'].replace({'Republic of Korea':'South Korea','United States of America':'United States','United Kingdom of Great Britain and Northern Ireland':'United Kingdom','United States of America':'United States','China, Hong Kong Special Administrative Region':'Hong Kong'})
    energy['Country'] = energy['Country'].str.replace(r"\s+\(.*\)","")
#    print(energy.shape)
    
    GDP = pd.read_csv('world_bank.csv',skiprows=4)
    GDP['Country Name']=GDP['Country Name'].replace({'Korea, Rep.':'South Korea','Iran, Islamic Rep.':'Iran','Hong Kong SAR, China':'Hong Kong'})
    GDP = GDP[['Country Name','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']]
    GDP.columns = ['Country','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
#    print(GDP.shape)
    
    ScimEn = pd.read_excel(io='scimagojr-3.xlsx')
    ScimEn = ScimEn[:15]
#    print(ScimEn.shape)
    
    df1 = pd.merge(ScimEn,energy, how='inner', left_on='Country', right_on='Country')
    final_df = pd.merge(df1,GDP, how='inner', left_on='Country', right_on='Country')
    final_df = final_df.set_index('Country')
    return final_df

print(answer_one())

def answer_two():
    import pandas as pd
    import numpy as np
    energy = pd.read_excel('Energy Indicators.xls', skip_footer=38, skiprows=17, parse_cols='C:F')
    col_names = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy.columns = col_names
    energy.loc[energy['Energy Supply'] == '...'] = np.NaN
    energy[['Energy Supply', 'Energy Supply per Capita']] = energy[['Energy Supply', 'Energy Supply per Capita']].apply(pd.to_numeric)
    energy['Energy Supply'] = energy['Energy Supply']*10**6
    energy['Country'] = energy['Country'].str.replace(r" \(.*\)","")
    energy['Country'] = energy['Country'].str.replace(r"([0-9]+)$","")
    replace_dict={"Republic of Korea": "South Korea",
                  "United States of America": "United States",
                  "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                  "China, Hong Kong Special Administrative Region": "Hong Kong"}
    energy['Country'].replace(to_replace=replace_dict, inplace=True)
    energy.reset_index()
    energy = energy.set_index('Country')
    en_shape = energy.shape
    
    GDP = pd.read_csv('world_bank.csv', skiprows=4)
    replace_dict = {"Korea, Rep.": "South Korea", 
                    "Iran, Islamic Rep.": "Iran",
                    "Hong Kong SAR, China": "Hong Kong"
                   }
    GDP['Country Name'].replace(to_replace=replace_dict, inplace=True)
    years_to_keep = np.arange(2006, 2016).astype(str)
    GDP = GDP[np.append(['Country Name'],years_to_keep)]
    GDP.reset_index()
    GDP = GDP.rename(columns={'Country Name': 'Country'})
    GDP = GDP.set_index('Country')
    GDP_shape = GDP.shape
    
    ScimEn = pd.read_excel('scimagojr-3.xlsx', header=0)
    ScimEn.reset_index()
    ScimEn = ScimEn.set_index('Country')
    ScimEn_shape = ScimEn.shape
    
    first_merge = pd.merge(energy, GDP, how='outer', left_index=True, right_index=True)
    result = pd.merge(ScimEn, first_merge, how='outer', left_index=True, right_index=True)
    #result = result.reset_index().dropna(thresh=result.shape[1]-10).set_index('Country')
    result = result.shape[0]-15
    
    return result

print(answer_two())

def answer_three():
    Top15 = answer_one()
    avgGDP = Top15[['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']].mean(axis=1).rename('avgGDP').sort_values(ascending=False)
    return avgGDP

print(answer_three())

def answer_four():
    Top15 = answer_one()
    six = Top15.iloc[3,19] - Top15.iloc[3,10]
    return six
print(answer_four())

def answer_five():
    Top15 = answer_one()
    m = Top15.iloc[:,8].mean()
    return m

print(answer_five())

def answer_six():
    Top15 = answer_one()
    result = Top15['% Renewable'].idxmax()
    return (result, Top15.loc[result, '% Renewable'])

print(answer_six())

def answer_seven():
    Top15 = answer_one()
    Top15['Citation Ratio'] = Top15['Self-citations']/Top15['Citations']
    ans = Top15[Top15['Citation Ratio'] == max(Top15['Citation Ratio'])]
    return (ans.index.tolist()[0],ans['Citation Ratio'].tolist()[0])

print(answer_seven())

def answer_eight():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15 = Top15.sort_values(['PopEst'], ascending=False)
    Top15 = Top15.reset_index()
    return Top15.loc[2, 'Country']
print(answer_eight())

def answer_nine():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    ans = Top15['Citable docs per Capita'].corr(Top15['Energy Supply per Capita'])
    return ans

print(answer_nine())

def plot9():
    import matplotlib as plt
#    %matplotlib inline
    
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])
    
#print(plot9())
    
def answer_ten():
    Top15 = answer_one()
    Top15['HighRenew'] = [1 if x >= Top15['% Renewable'].median() else 0 for x in Top15['% Renewable']]
    return Top15['HighRenew']
print(answer_ten())


def answer_eleven():
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
    Top15 = answer_one()
    Top15['PopEst'] = (Top15['Energy Supply'] / Top15['Energy Supply per Capita']).astype(float)
    Top15 = Top15.reset_index()
    Top15['Continent'] = [ContinentDict[country] for country in Top15['Country']]
    ans = Top15.set_index('Continent').groupby(level=0)['PopEst'].agg({'size': np.size, 'sum': np.sum, 'mean': np.mean,'std': np.std})
    ans = ans[['size', 'sum', 'mean', 'std']]
    return ans
print(answer_eleven())

def answer_twelve():
    Top15 = answer_one()
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
    Top15 = Top15.reset_index()
    Top15['Continent'] = [ContinentDict[country] for country in Top15['Country']]
    Top15['bins'] = pd.cut(Top15['% Renewable'],5)
    return Top15.groupby(['Continent','bins']).size()

print(answer_twelve())

def answer_thirteen():
    import numpy as np
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15['PopEst'] = Top15['PopEst'].apply('{:,}'.format)
    return Top15['PopEst']   

print(answer_thirteen())

def plot_optional():
    import matplotlib as plt
#    %matplotlib inline
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. \
This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
2014 GDP, and the color corresponds to the continent.")
    
#plot_optional()
    
    