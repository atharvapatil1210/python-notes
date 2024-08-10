'''It is perform when our task is repeatable'''
'''
Types of Functions
1.Built-in
2.User Defined
Create a function
    def function_name (parameters):
        #statement
        Return expression
Calling a function
    function_name(argument1, argument2)'''

def HelloWorld () :
    print("Helloworld")
    return "Hello"
HelloWorld()

'''
Types of Arguments 
'''
def add(n1,n2):
    print("n1",n1)
    print("n2",n2)
    sum = n1+n2
    return sum

#positional argument
print("The sum is",add(3,2))
print(add(34,12))

#keyword argument
print("The sum is",add(n2=2 , n1=1))

'''default argument---> at the time of defined function this is used
    def sum(n2 , n1=0)'''

'''Arbitrary arguements(variable-length aguements * args and **kwargs)'''

def addAllNumbers(*args):
    sum = 0 
    for i in args:
        sum += 1
    return sum

output = addAllNumbers(1,2,3,4,5)
print("The sum of ",output)

def studentInfo(**kwargs):
    for x ,y in kwargs.items():
        print(x,"is",y)

studentInfo(name="rutuja",age=20, city="akola")
studentInfo(name="punam",age=20,city="akola")