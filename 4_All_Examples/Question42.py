#Q42] Python Program to Illustrate Different Set Operations

set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,1}

#Intersection
set3 = set1 & set2
print(f"Intersection : {set3}")

#Union
set3 = set1 | set2
print(f"Union : {set3}")

#Difference
set3 = set1 - set2
print(f"Difference : {set3}")

#symmetric Difference
set3 = set1 ^ set2
print(f"Symmetric Difference : {set3}")
 