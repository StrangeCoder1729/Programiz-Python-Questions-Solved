#Q13] Python Program to Find Factorial of Number Using Recursion

def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num-1)



num = int(input("Enter number : "))

print(fact(num))