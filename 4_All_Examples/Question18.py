#Q18} Python Program to Print the Fibonacci sequence


def fib(n):
    
    i = 0
    n1 = 0
    n2 = 1
    temp = 0
    while(i < n):
        
        temp = n1 + n2
        n1 = n2
        n2 = temp
        print(temp,end=' ')
        i+=1


n = int(input("Enter range : "))

fib(n)