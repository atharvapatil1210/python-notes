input_string = input("Enter String : ")
n = int(input("Enter n : "))

#creating dictonary for mirror opearation 
alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabets = alphabets[::-1]
dict1 = dict(zip(alphabets,reverse_alphabets))

#finding the part of string on which we will do mirror operation
prefix = input_string[0:n-1]
suffix = input_string[n-1:]

#finding the mirror string 
mirror = ""
for i in range(0,len(suffix)):
    mirror = mirror + dict1[suffix[i]]

#creating the final string 
res = prefix + mirror
print("The result is ",res)