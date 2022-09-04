#Q73]  Python Program to Delete an Element From a Dictionary

n = int(input("Enter n : "))

dict1 = dict(input("Enter key-value pair : ").split() for _ in range(0,n))

key = input("Enter element(key) you wanna delete : ")

del dict1[key]
print(dict1)