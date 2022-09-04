#Q13] Python Program to Sort a Dictionary by Value

n = int(input("Enter n : "))
d1 = dict((input("Enter key-value pair : ").split() for _ in range(0,n)))

sorted_d1 = dict(sorted(d1.items(), key = lambda x: x[1]))
print(sorted_d1)