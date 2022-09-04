#Q6] Python Program to Swap Two Variables without using third variable

print("Befor SwappingL-")
a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))

a = a+b
b = a-b
a = a-b

print()
print("After Swapping:-")
print("Number 1 : {}".format(a))
print("Number 2 : {}".format(b))
