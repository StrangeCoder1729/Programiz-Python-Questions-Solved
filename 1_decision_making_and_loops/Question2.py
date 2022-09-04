# Q2] Python Program to Check if a Number is Odd or Even

num = int(input("Enter number : "))

if num % 2 == 0:
    print("{} is an even number".format(num))
elif num % 2 == 1:
    print("{} is an odd number".format(num))