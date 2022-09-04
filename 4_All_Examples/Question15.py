#Q15] Python Program to Print all Prime Numbers in an Interval


def prime(temp_num):
    isprime = True

    for i in range(2,temp_num):
        if(temp_num % i == 0):
            isprime = False
            break
    if(isprime == True):
        return temp_num


num1 = int(input("Enter n1 : "))
num2 = int(input("Enter n2 : "))

for i in range(2,num2):
    if(prime(i) == None):
        continue
    print(prime(i),end= ' ')