#Q28]  Python Program to Convert Two Lists Into a Dictionary



lst1 = list(map(str,input("Enter series of numbers for list 1 : ").split()))
lst2 = list(map(int,input("Enter Series of numbers for list 2 : ").split()))

dict1 = {}
 
if(len(lst1) == len(lst2)):
    for i in range(0,len(lst2)):
        dict1.update({lst1[i]:lst2[i]})

print(dict1)