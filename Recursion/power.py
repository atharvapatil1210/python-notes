def power(a,b):
    #base function
    if b == 0 :
        return 1
    #recursive case 
    ans = a * power(a,b-1)
    return ans

a = int(input("Enter a value of a "))
b = int(input("Enter a value of b "))

print(power(a,b))