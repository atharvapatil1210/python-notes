n = int(input("Enter size fo list"))

list = []
for _ in range(n):
    num = int(input())
    list.append(num)

idx1 = int(input("Enter index1 : "))
idx2 = int(input("Enter index2 : "))

#swapping the value of index1 and index2 
temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp

print(list)
