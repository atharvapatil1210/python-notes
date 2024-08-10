l1 = [1,2,3,45]
l2 = [2,23,42,31]
l3 = [23,1,3,5]

s1 = set(l1)
s2 = set(l2)
s3 = set(l3)

s1s2 = s1.intersection(s2)
final_set = s1s2.intersection(s3)

final_list = list(final_set)
print(final_list)