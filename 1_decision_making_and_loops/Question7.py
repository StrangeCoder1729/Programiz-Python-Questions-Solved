#Q7] Python Program to Find the Factorial of a Number

 
def fact(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return num * fact(num-1)

num = int(input("Enter number : "))
res = fact(num)
print(res)