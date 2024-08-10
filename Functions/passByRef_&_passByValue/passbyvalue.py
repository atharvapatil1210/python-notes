'''
Pass by value --> For Immutable Objects - strings , integers , float , tuples 
-> when passed to function , a copy of the objects is created
immutable means copy of objects are to be created or do not affect the original value'''

def addOne(x):
    x +=1
    print("Inside function: ",x)

x = 5 
addOne(x)
print("Outside function:",x)