# Example 1: Access both key and value using items()

 
n = int(input("Enter range : "))
d = dict((input("Enter key values pairs: : ").split() for _ in range(0,n)))

for key,value in d.items():
    print(key,value)

 