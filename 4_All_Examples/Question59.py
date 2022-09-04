#Q59] Python Program to Check if a Key is Already Present in a Dictionary

n = int(input("Enter n : "))
d1 = dict(input("Enter key-value pair : ").split() for _ in range(0,n))
 
user_key = input("Enter key : ")
ispresent = False
for key in d1.keys():
    if(user_key == key):
        ispresent = True 
        break


if(ispresent):print("Key is present in the dictionary")
else:print("Key is not present in the dictionary")