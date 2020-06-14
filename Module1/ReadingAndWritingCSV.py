# -*- coding: utf-8 -*-

import csv
#%precision 2

with open("mpg.csv") as csvfile:
    mpg = list(csv.DictReader(csvfile))
    
print(mpg[:3]) # The first three dictionaries in our list.

#csv.Dictreader has read in each row of our csv file as a dictionary.
#len shows that our list is comprised of 234 dictionaries.

print(len(mpg))


#keys gives us the column names of our csv.
print(mpg[0].keys())


#This is how to find the average cty fuel economy across all cars. 
#All values in the dictionaries are strings, so we need to convert 
#to float.
print(sum(float(d['cty']) for d in mpg) / len(mpg))

#Similarly this is how to find the average hwy fuel economy across all cars.
print( sum(float(d['hwy']) for d in mpg) / len(mpg))

#Use set to return the unique values for the number of cylinders the cars in our dataset have.
cylinders = set(d['cyl'] for d in mpg)
print(cylinders)

#Here's a more complex example where we are grouping the cars by number of cylinder, 
#and finding the average cty mpg for each group.
CtyMpgByCyl = []

for c in cylinders:
    summpg = 0
    cyltypecount =  0
    for d in mpg:
        if(d['cyl'] == c):
            summpg += float(d['cyl'])
            cyltypecount += 1
    
    CtyMpgByCyl.append((c, summpg / cyltypecount))
    
CtyMpgByCyl.sort(key=lambda x: x[0])    
print(CtyMpgByCyl)


#Use set to return the unique values for the class types in our dataset.
vehicleclass = set(d['class'] for d in mpg) 
print(vehicleclass);

#And here's an example of how to find the average hwy mpg for each class of 
#vehicle in our dataset.
HwyMpgByClass = []

for v in vehicleclass:
    summpg = 0
    vclasscount = 0
    for d in mpg:
        if(d['class'] == v):
            summpg += float(d['hwy'])
            vclasscount += 1
    HwyMpgByClass.append((v, summpg / vclasscount))
    
    HwyMpgByClass.sort(key=lambda x: x[1])
print(HwyMpgByClass)
    
    



























