names = {"punam","rutuja","ria"}

print(names)

print(len(names))

print(type(names))

for x in names:
    print(x)

if "punam" in names:
    print("Sia is in the set")

names.add("atharva")
print(names)

names.remove("atharva")
print(names)


names.discard("sia")
print(names)