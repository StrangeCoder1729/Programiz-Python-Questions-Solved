# Q54] Python Program to Sort a Dictionary by Value

n = int(input("Enter n : "))
dict1 = dict(input("Enter key-value : ").split() for _ in range(0,n))
 

sorted_dict1 = {key:value for key,value in sorted(dict1.items() ,key = lambda item:item[1])}

print(sorted_dict1)