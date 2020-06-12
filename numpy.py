# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 03:12:04 2020

@author: shari
"""

import numpy as np
mylist = [1, 2, 3]
x = np.array(mylist)

#Or just pass in a list directly
y = np.array([4, 5, 6])
print(y)

#Pass in a list of lists to create a multidimensional array.
m = np.array([[7, 8, 9], [10, 11, 12]])
print(m)


#Use the shape method to find the dimensions of the array. (rows, columns)
print(m.shape)

#arange returns evenly spaced values within a given interval.
n = np.arange(0,30,2)
print(n)

#reshape returns an array with the same data with a new shape.
n = n.reshape(3, 5) #reshape array to be 3x5
print(n)

#arange returns evenly spaced values within a given interval.
n = np.arange(0,50,5)
print(n)

#reshape returns an array with the same data with a new shape.
n = n.reshape(2, 5) #reshape array to be 3x5
print(n)

#linspace returns evenly spaced numbers over a specified interval.
print("#linspace returns evenly spaced numbers over a specified interval.")
o = np.linspace(0,10,6)
print(o)

print("#linspace returns evenly spaced numbers over a specified interval.")
o = np.linspace(0,4,9) #here, 0 to 4 interval ke 9 vag kora hoyeche.
print(o)

print("#resize changes the shape and size of array in-place.")
o.resize(3,3)
print(o)

print("#ones returns a new array of given shape and type, filled with ones.")
print(np.ones((3, 2)))  

print("#zeros returns a new array of given shape and type, filled with zeros.")
print(np.zeros((3, 2)))  

print("#eye returns a 2-D array with ones on the diagonal and zeros elsewhere.")
print(np.eye(3))      

print("#diag extracts a diagonal or constructs a diagonal array.")
print(np.diag(y))


print("#Create an array using repeating list (or see np.tile)")
print(np.array([1, 2, 3] * 3))

print("#Repeat elements of an array using repeat.")
print(np.repeat([1, 2, 3], 3))      

print("#Combining Arrays")
p = np.ones([2, 3], int)
print(p)

print("#Use vstack to stack arrays in sequence vertically (row wise)")
print(np.vstack([p, 2*p]))

print("#Use hstack to stack arrays in sequence horizontally (column wise).")
print(np.hstack([p, 2*p]))

# =============================================================================
# #Use +, -, *, / and ** to perform element wise addition, subtraction, multiplication, division and power
# =============================================================================
print("#Use +, -, *, / and ** to perform element wise addition, subtraction, multiplication, division and power.")
print([1,2] + [3,4])

print("#As these lists are arry so we can perform addition, subtraction, multiplication, division and power")
print(x + y) # elementwise addition     [1 2 3] + [4 5 6] = [5  7  9]
print(x - y) # elementwise subtraction  [1 2 3] - [4 5 6] = [-3 -3 -3]

print(x * y) # elementwise multiplication  [1 2 3] * [4 5 6] = [4  10  18]
print(x / y) # elementwise divison         [1 2 3] / [4 5 6] = [0.25  0.4  0.5]

print(x**2) # elementwise power  [1 2 3] ^2 =  [1 4 9]

# =============================================================================
# Dot Product
# =============================================================================
print("#Dot Product:")
x.dot(y) # dot product  1*4 + 2*5 + 3*6
print(x.dot(y))

z = np.array([y, y**2])
print(z)
print(len(z)) # number of rows of array

print("#Let's look at transposing arrays. Transposing permutes the dimensions of the array.")
z = np.array([y, y**2])
print(z)
print(z.shape)

print("#Use .T to get the transpose.")
print(z.T)

print("#The number of rows has swapped with the number of columns")
print(z.T.shape)

print("#Use .dtype to see the data type of the elements in the array.")
print(z.dtype)      

print("#Use .astype to cast to a specific type.")
z = z.astype('f')
print(z.dtype)

# =============================================================================
#    Math Functions
# =============================================================================

print("#Numpy has many built in math functions that can be performed on arrays.")
a = np.array([-4, -2, 1, 3, 5])      

print(a.sum())
print(a.max())
print(a.min())
print(a.mean())
print(a.std())

print("#argmax and argmin return the index of the maximum and minimum values in the array.")

print(a.argmax())
print(a.argmin())

# =============================================================================
# Indexing / Slicing
# =============================================================================
s = np.arange(13)**2
print(s)

print("#Use bracket notation to get the value at a specific index. Remember that indexing starts at 0.")
print(s[0])
print(s[4])
print(s[-1])

#Use : to indicate a range. array[start:stop]
#Leaving start or stop empty will default to the beginning/end of the array.
print(s[2:6])


#Use negatives to count from the back.
print(s[-4:])

#A second : can be used to indicate step-size. array[start:stop:stepsize]
#Here we are starting 5th element from the end, and counting backwards by 2 
#until the beginning of the array is reached.

print(s[-5::-2])


print("#Let's look at a multidimensional array.")
r = np.arange(36)
r.resize((6, 6))
print(r)

print("#Use bracket notation to slice: array[row, column]")
print(r[2, 2])      

print("#Here we are selecting all the rows up to (and not including) row 2, and all the columns up to (and not including) the last column")
print(r[:2, :-1])

print("#This is a slice of the last row, and only every other element.")
print(r[-1, ::2])

print("#We can also perform conditional indexing. Here we are selecting values from the array that are greater than 30. (Also see np.where)")
print(r[r>30])

print("#assign 30 to every index of r which has value greater than 30")
r[r>30] = 30
print(r)

# =============================================================================
# Copying Data
# =============================================================================

#Be careful with copying and modifying arrays in NumPy!
#
#r2 is a slice of r
r2 = r[:3, :3]
print(r2)

print("#Set this slice's values to zero ([:] selects the entire array)")
r2[:] = 0
print(r2)

print("#r has also been changed!")
print(r)

print("#To avoid this, use r.copy to create a copy that will not affect the original array")   
r_copy = r.copy()
print(r_copy)

print("#Now when r_copy is modified, r will not be changed")
r_copy[:] = 10
print(r_copy, '\n')
print(r)


print("#Iterating Over Arrays")
print("#Let's create a new 4 by 3 array of random numbers 0-9.")      
test = np.random.randint(0, 10, (4,3))      
print(test)


print("#Iterate by row:")
for row in test:
    print(row)

print("#Iterate by index:")
for i in range(len(test)):
    print(test[i])


print("#Iterate by row and index:")
for i, row in enumerate(test):
    print('row', i, 'is', row)

print("#Use zip to iterate over multiple iterables")
test2 = test**2
print(test2)

for i, j in zip(test, test2):
    print(i,'+',j,'=',i+j)
