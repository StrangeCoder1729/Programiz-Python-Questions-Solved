#Q32] Python Program to Display Fibonacci Sequence Using Recursion

def fib(temp_i):
    if (temp_i == 0):
        return 0
    elif(temp_i == 1):
        return 1
    else:
        return fib(temp_i - 1)+ fib(temp_i -2)


n = int(input("Enter range : "))

for i in range(0,n):
    print(fib(i),end=' ')