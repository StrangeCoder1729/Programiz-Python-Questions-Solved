#Q11] Python Program to Display Fibonacci Sequence without using Recursion



def fib(n):
    n1 = 0
    n2 = 1
    temp = 0
    i = 0
    print(n1,n2,end =' ')
    while(i<n):

        temp = n1+n2
        n1 = n2
        n2 = temp
        print(temp,end =' ')
        i+=1
    

n = int(input("Enter range : "))
fib(n)
    

