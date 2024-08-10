''''arithmetic operator
addition ----> +
subtraction -----> -
Multiplication ----> *
Division ------> /
Modouls ------> %
'''

print("Sum:",2+3)
print("Difference",5-4)
print("Multiplication",3*3)
print("Division",3/2)
print("Remainder",5%3)

#assignement opt
n1 = 3
n2 = 5
print(n1,n2)

n2+=2
print(n1,n2)


#comparision Opt
print("== Equal to")
print("!= not equal")
print("> greter than")
print("< less than")
print(">= greater than equal to ")
print("<= Less than equal to ")

n1 = 34
n2 = 32
print(n1>n2)

#Logical Operaytor
# Mathematical logic table
print(2>4 and 4<3)
print(2>4 or 3<23)
print(not(2>3))

#Identity operator
print("atharva" is "atharva")

print("atharva" is not "atharva")

#Membership operators

fruits = ["apple","bannan","mango"]
print("apple" in fruits)
print("safarchand" not in fruits)

#Bitwise Operator
'''0 and 1 are Bitwise operator'''
print("Binary resp")
#Number conversion

a = 23
b = 23

print(a & b)
print(a | b)
print(a ^ b )

#Operator Precedance
print("BODMAS")
print("() ---> ** ---> / ---> // ---> * ---> + ----> - ---> >> ----> << ----> & ----> | ---> ^ ----> comparision opt ---> ")

a = 2 
b = 3
c = 5 
a_str = str(a)
b_str = str(b)
c_str = str(c)

final_string = a_str + b_str + c_str

final_int = int(final_string)

print(final_string)
print(final_int)