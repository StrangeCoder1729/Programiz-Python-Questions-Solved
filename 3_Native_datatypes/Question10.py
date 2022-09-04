# Q10] Python Program to Access Index of a List Using for Loop


lst = list(map(int,(input("Enter list of numbers : ")).split(' ')))

print("Index Elements")
for i in range(0,len(lst)):
    print(f"{i}         {lst[i]}")