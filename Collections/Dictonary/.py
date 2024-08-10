phones = {
    "john" : 88322,
    "raghavi" : 232132,
    "joy" : 2323232
}
print(phones["john"])
print(type(phones))
print(len(phones))

phones["john"] = 2323213
print(phones)

more_phone = {
    "kia" : 2312121
}
phones.update(more_phone)
print(phones)

for x,y in phones.items():
    print(x,y)

phones = {
    "Area1":{
        "x" : 0,
        "y" : 1,
        "z" : 2
    },
    "Area2":{
        "x" : 0,
        "y" : 1 ,
        "z" : 2
    }
}
print(phones)