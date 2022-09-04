#Q5] Python Program to Check Prime Number

def prime(num):
    
    isprime = True
    for i in range(2,num):
        if(num % i == 0):
            isprime = False
            break
    
    if (isprime == True):
        print("{} is a Prime number".format(num))
    else:
        print("{} is not a Prime number".format(num))


num = int(input("Enter number : "))

prime(num)