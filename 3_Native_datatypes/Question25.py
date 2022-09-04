#Q25] Python Program to Count the Occurrence of an Item in a List

 

lst = list(map(str, input("Enter series of numbers : ").split()))

d1 = {}
counting = 0
for i in range(0,len(lst)):
    counting = lst.count(lst[i])

    # print(lst[i], countng)
    d1.update({lst[i]:counting})

print(d1)


