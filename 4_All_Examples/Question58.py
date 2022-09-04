# Q58] Python Program to Concatenate Two Lists


lst1 = list(map(int,input("Enter Series of numbers for list 1 : ").split()))

lst2 = list(map(int,input("Enter Series of numbers for list 2 : ").split()))

lst3 = []
 
for num1 in lst1: lst3.append(num1)
for num2 in lst2: lst3.append(num2)
print(lst3)