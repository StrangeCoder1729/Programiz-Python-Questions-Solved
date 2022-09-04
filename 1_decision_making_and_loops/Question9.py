#Q9}Python Program to Print the Fibonacci sequence


def fib(num):
    if num == 0:
        return 0

    elif num == 1:
        return 1
    
    else:
        return fib(num - 1) + fib(num - 2)


num = int(input("Enter range : "))

for i in range(0,num):
    print(fib(i))