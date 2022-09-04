# Example 2: Access both key and value without using items()


n = int(input("Enter range : "))

d2 = dict((input("Enter key and value : ").split() for _ in range(0,n)))
print(d2)


for key in d2:
    print(key,d2[key])