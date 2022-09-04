# Q9] Python Program to Merge Two Dictionaries

n = int(input("Enter range : "))

print("Dictionary 1 :-")
d1 = dict((input("Enter key-value pair : ")).split() for _ in range(0,n))
print(d1)
print()

print("Dictionary 2 :-")
d2 = dict((input("Enter key-value pair : ")).split() for _ in range(0,n))
print(d2)

dict3 = {}

for key,value in d1.items():
    dict3.update({key:value})
    # print(key,value)

for key,value in d2.items():
    dict3.update({key:value})
    # print(key,value)

print()
print("Merging both the Dictionaries:-")
print(dict3)