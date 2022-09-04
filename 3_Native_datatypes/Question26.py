# Q26] Python Program to Delete an Element From a Dictionary

n = int(input("Enter n : "))
d1 = dict(input("Enter key-value pair : ").split() for _ in range(0,n))
print()
print(d1)
delete = input("Enter which element to delete : ")
del d1[delete]
print()
print("After Deleting the element :-")

print(d1)