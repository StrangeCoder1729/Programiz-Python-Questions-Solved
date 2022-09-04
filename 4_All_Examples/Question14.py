#Q14] Python Program to Check Prime Number

def prime(temp_num):
    isprime = True

    for i in range(2,num):
        if(num % i == 0):
            isprime = False
            break
    if(isprime == True):
        print("Its a Prime Number !!")
    else:
        print("It is not a Prime Number !!")


num = int(input("Enter the number : "))
prime(num)