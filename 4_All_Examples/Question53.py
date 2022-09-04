#Q53] Python Program to Iterate Over Dictionaries Using for Loop

n = int(input("Enter n : "))
d = dict(input("Enter key-value pair : ").split() for _ in range(0,n))

for key,value in d.items():
    print(key,value)