#Q16] Python Program to Check if a Key is Already Present in a Dictionary

def present_key(temp_key,temp_d1):
    
    lst_keys = list(temp_d1.keys())
   
    if temp_key in lst_keys:
        print("Key is present")
    else:
        print("Key is not present")

n = int(input("Enter n : "))
d1 = dict((input("Enter Key-value pair : ")).split() for _ in range(0,n))
print(d1)
key = input("Enter key : ")
present_key(key,d1)
# print(res1
 

