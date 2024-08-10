''''
rows 
columns 
what to print 

**********
**********'''

# n = int(input("Enter n : "))

# for _ in range(n):
#     print("*"*5)

n = 5

for i in range(n):
    for j in range(1 ,n+1):
        print(j,end=" ")
    print()