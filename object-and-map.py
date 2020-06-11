# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 12:44:03 2020

@author: shari
"""

class Person:
    department = "School of Information" #a class variable
    
    def set_name(self, new_name): #a method
        self.name = new_name
        
    def set_location(self, new_location):
        self.location = new_location
        
person = Person()
person.set_name('Christoper Brooks')
person.set_location('Ann Arbor , MI, USA')

print('{} live in {} and works in the department {}'.format(person.name, person.location, person.department))


#Here's an example of mapping the min function between two lists.
store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]

cheapest = map(min, store1, store2)
print(cheapest)

#Now let's iterate through the map object to see the values.
for item in cheapest:
    print(item)




