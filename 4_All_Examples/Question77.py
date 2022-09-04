# Q77] Python Program to Convert Two Lists Into a Dictionary


lst1 = [num for num in input("Enter for list 1 : ").split()]
lst2 = [num for num in input("Enter for list 2 : ").split()]

len_lst = 0

if(len(lst1) > len(lst2)):
    len_lst = len(lst2)
elif(len(lst1) < len(lst2)):
    len_lst = len(lst1)
else:
    len_lst=len(lst1)

dict1 = {}

for i in range(0,len_lst):
    dict1.update({lst1[i]:lst2[i]})

print(dict1)