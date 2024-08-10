fruits = ["apple","mango","cherry"]
print(fruits)
print(type(fruits))
print(len(fruits))

# if an item present in list
if "mango" in fruits:
    print("Mango is in fruits")

print(fruits[1])

print(fruits[0:2])
fruits.append("kiwi")
print(fruits)
fruits.remove("kiwi")
print(fruits)
fruits.insert(2,"kiwi")
print(fruits)

fruits.pop(1)
print(fruits)

fruits[1:2] = ["papaya"]
print(fruits)

#sorting a list
fruits.sort(reverse=True)
print(fruits)