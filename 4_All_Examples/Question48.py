#Q48 Python Program to Merge Two Dictionaries

n = int(input("Enter n : "))
print("d1:-")
d1 = dict(input("Enter key:value pair : ").split() for _ in range(0,n))
print()
print("d2:-")
d2 = dict(input("Enter key:value pair : ").split() for _ in range(0,n))

print()
print("Dictionary 1:-")
print(d1)
print()
print("Dictionary 2:-")
print(d2)
print()

for key,value in d2.items():
    d1.update({key:value})


print("Merging bothe dictionaries :-")
print(d1)
