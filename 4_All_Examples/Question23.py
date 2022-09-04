#Q23] Python Program to Find Numbers Divisible by Another Number

num = int(input("Enter number : "))

for i in range(2,num):
    if(num % i == 0):
        print(i,end=' ')
