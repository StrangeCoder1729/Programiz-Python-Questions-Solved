#Q4] Python Program to Print all Prime Numbers in an Interval

def prime(n2):
    isprime = True

    for i in range(2,n2):
        if(n2 % i == 0):
            isprime = False
            break
    if (isprime == True):
        return n2


n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))

for i in range(n1,n2):
    if(prime(i) == None):
        continue
    print(prime(i),end=' ')