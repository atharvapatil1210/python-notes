name1 = 'ram'
name2 = "ramisBest"
name3 = '''KingisNotBest_KingMakerIsBest'''

#traversing a string
#using for loop
for i in name1:
    print(i)

#using list comprehension
#list = [char for char in name1]
'''
Positive indexing and negative indexing are two types for indexing of string
'''
print(name1.capitalize())
print(name2.lower())
print(name3.replace("King","ram"))
print(name1,2)
print(name1+name2)
str = "The Name of the boy is {s} , and he is a {m}".format(s=name1,m=name2)
print(str)

'''Escape Character'''
#xhh for hexadecimal val
text = "The unexpected always happen"

print(len(text))
print(text[:11])
print(text.replace('always','never'))
text2 = "No matter what"
new_text = name1 + text2
print(new_text)