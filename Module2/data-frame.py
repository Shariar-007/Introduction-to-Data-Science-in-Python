# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 02:09:49 2020

@author: shari
"""
# =============================================================================
# The DataFrame Data Structure
# =============================================================================
import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})

purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})

purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

print(df)
print(df.loc['Store 2'])
print(type(df.loc['Store 2']))
print(df.loc['Store 1'])
print(df.loc['Store 1', 'Cost'])
print(df.T)
print(df.T.loc['Cost'])
print(df['Cost'])
print(df.loc['Store 1']['Cost'])
print(df.loc[:,['Name', 'Cost']])

df.drop('Store 1')
print(df)

copy_df = df.copy()
copy_df = copy_df.drop('Store 1') #row delete
print(copy_df)

del copy_df['Name'] #column delete
print(copy_df)

df['Location'] = None
print(df)
