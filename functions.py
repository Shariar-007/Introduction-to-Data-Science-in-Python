#Function Practise

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
