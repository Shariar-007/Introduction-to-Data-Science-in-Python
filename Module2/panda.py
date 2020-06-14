
# =============================================================================
# 
# The Series Data Structure
# =============================================================================
import pandas as pd

animals = ['Tiger', 'Bear', 'Moose']
animals = pd.Series(animals)
print(animals)

numbers = [1, 2, 3]
pd.Series(numbers)
print(pd.Series(numbers))

animals = ['Tiger', 'Bear', None]
pd.Series(animals)

print(pd.Series(animals))

numbers = [1, 2, None]
pd.Series(numbers)
print(pd.Series(numbers))

import numpy as np


print(np.nan == None)
print(np.isnan(np.nan))

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'
          }
s = pd.Series(sports)
print(s)
print(s.index)

s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
print(s)

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}

s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
print(s)

# =============================================================================
# Querying a Series
# =============================================================================
print("#Querying a Series")
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
print(s)
print(s.iloc[3])
print(s.loc['Golf'])
print(s[3])
print(s['Golf'])

sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'
          }
s = pd.Series(sports)

#print(s[0]) #This won't call s.iloc[0] as one might expect, it generates an error instead

s = pd.Series([100.00, 120.00, 101.00, 3.00])
print(s)

#this type of iteration takes much time so try to use panda or numpy library
total = 0
for item in s:
    total+=item
print(total)

import numpy as np

total = np.sum(s)
print(total)

print("#this creates a big series of random numbers")
s = pd.Series(np.random.randint(0,1000,10000))
print(s.head())
print(len(s))

summary = np.sum(s)
print(summary)

s+=2
print(s.head())

for label, value in s.iteritems():
    s.set_value(label, value+4)
print(s.head())

s = pd.Series(np.random.randint(0,1000,10000))
for label, value in s.iteritems():
    s.loc[label]= value+2

s = pd.Series(np.random.randint(0,1000,10000))
s+=2

s = pd.Series([1, 2, 3])
s.loc['Animal'] = 'Bears'
print(s)

original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'
                             })

cricket_loving_countries = pd.Series(['Australia',
              'Barbados',
              'Pakistan',
              'England'], 
              index=['Cricket',
                'Cricket',
                'Cricket',
                'Cricket'])

all_countries = original_sports.append(cricket_loving_countries)

print(original_sports)
print(cricket_loving_countries)
print(all_countries)
print(all_countries.loc['Cricket'])







