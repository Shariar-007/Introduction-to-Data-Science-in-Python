# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 02:26:41 2020

@author: shari
"""

#Here's an example of lambda that takes in three parameters and adds the first two.
my_function = lambda a, b, c : a + b
my_function(1,2,3)

print(my_function(1,2,3))

my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)
#print(my_list)

my_list = [number for number in range(0,1000) if number % 2 ==0 ]
#print(my_list)

#lambda Question
#people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
#
#def split_title_and_name(person):
#    return person.split()[0] + ' ' + person.split()[-1]

#option 1
#for person in people:
#    print(split_title_and_name(person) == (lambda person:???))

#option 2
#list(map(split_title_and_name, people)) == list(map(???))
    
#ANSWER
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
 
def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]
# 
# #option 1
for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))
 
# #option 2
list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))    


people1 = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
 
def split_title_and_name1(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

x = list(map(split_title_and_name1, people1))
 
print(x)
 