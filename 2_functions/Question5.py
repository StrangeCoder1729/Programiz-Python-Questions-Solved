# Q5] Python Program to Find HCF or GCD

 

def hcf(num1,num2):
    smaller = 0
    h = 0
    if(num1 > num2):
        smaller = num2
    else:
        smaller = num1
    
    for i in range(1,smaller+1):
        if((num1 % i == 0) and (num2 % i == 0)):
            h = i
    return h



num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

res = 0
res = hcf(num1,num2)
print(f"HCF : {res}")

