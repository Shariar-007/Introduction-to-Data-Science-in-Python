#Function Practise
##################

def addNumbers(a,b):
    return a+b
print(addNumbers(2,5))



def myFunction(a,b,c=None):
    if(c == None):
        return a+b
    else: 
        return a+b+c
    
print(myFunction(1,2,3))




def addNumbers(x,y,z=None,flag=False):
    if(flag):
        print("Flag is True")
    if(z == None):
        return x+y
    else:
        return x+y+z
    
print(addNumbers(2,3))
print(addNumbers(2,3,4))

a = addNumbers
print(a(2,3,4))


#types and sequences
####################
print(type('This is a string'))
print(type(None))
print(type(addNumbers))
print(type(1.0))
print(type(1))

#Lists are a mutable data structure.
x = [1, 'a', 2, 'b']
print(type(x))

x.append(3)
print(x)

#Tuples are an immutable data structure (cannot be altered).
#can not be added or deleted or upated any item
x = (1, 'a', 2, 'b')
print(type(x))


#You can unpack a sequence into different variables:
#Make sure the number of values you are unpacking matches 
#the number of variables being assigned
x = ('Christopher', 'Brooks', 'brooksch@umich.edu')
fname, lname, email = x
print(fname)
print(lname)
print(email)


for item in x:
    print(item)

i=0
while(i!=len(x)):
    print(x[i])
    i = i+1

x = [1,2] + [3,4]
print(x)

x = [1] * 3
print(x)

x = [1,2,3,4,5]
print(x[0:1])
print(x[:1])
print(x[-3:-1])
print(x[2:])
print(1 in x)

x = "My Name is Shohag"
print(x[0:1])
print(x[3:])
print(x[-6:])
print(x[-1])

firstName = "Christopher"
lastName = "Brooks"
print(firstName +' ' +lastName)
print((firstName + ' ') * 3)
print(firstName + '2')
print(firstName + str(2))


#Dictionaries associate keys with values.

x = {
     "name": "Shohag",
     "age": 25,
     "sex": "male"
     }
print(type(x))

x["married"] = None
print(x)

#Iterate over all of the keys:
for item in x:
    print(item)

#Iterate over all of the values:
for item in x.values():
    print(item)

#Iterate over all of the items in the list:
for key,value in x.items():
    print(key)    
    print(value)  
    

#Python has a built in method for convenient string formatting.
details = "my name is {}. I am {} years old. I like {}"

details.format(x["name"], x["age"], x["sex"])

print(details.format(x["name"], x["age"], x["sex"]))

























