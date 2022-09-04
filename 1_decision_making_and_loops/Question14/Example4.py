# Example 4: Return keys or values explicitly

n = int(input("Enter range : "))

d4 = dict((input("Enter key and value : ")).split() for _ in range(0,n))

for key in d4.keys():
    print(key)

for value in d4.values():
    print(value)
