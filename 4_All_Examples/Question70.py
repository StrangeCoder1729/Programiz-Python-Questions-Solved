#Q70] Python Program to Count the Occurrence of an Item in a List


lst = list(map(int,input("Enter series of numbers : ").split()))

dict1 = {}

for i in lst:
    x = i
    y = lst.count(i)
    dict1.update({x:y})

print(dict1)