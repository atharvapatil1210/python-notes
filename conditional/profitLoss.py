costPrice = float(input("Enter Cost price : "))
sellPrice = float(input("Enter Selling Price : "))

if sellPrice > costPrice :
    print("It is profit of ",sellPrice-costPrice)
elif sellPrice == costPrice:
    print("No profit No loss")
else :
    print("It is loss of",costPrice-sellPrice)

'''
if condition1 :
    //statement1
elif condition2 :
    //statement2
elif condition3 ......:
    //statement3.....
else :
    //statement3 
'''
