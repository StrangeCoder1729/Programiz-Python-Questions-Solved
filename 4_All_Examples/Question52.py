#Q52] Python Program to Slice Lists

lst = list(map(int,input("Enter series of numbers : ").split()))

n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))

print("List Slicing from {0} to {1} : {2}".format(n1,n2,lst[n1:n2]))