#Q7] Python Program to Find the Factors of a Number

def factors(num):
    for i in range(1,num+1):
        if(num % i == 0):
            print(i)



num = int(input("Enter number : "))
factors(num)