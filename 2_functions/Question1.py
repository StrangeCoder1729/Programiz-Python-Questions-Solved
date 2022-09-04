#Q1] Python Program to Display Powers of 2 Using Anonymous Function


res1 = lambda a,b : f"{a} to Power {b} is {pow(a,b)}"

num1 = int(input("Enter Number : "))
n = int(input("Enter Power : "))

for i in range (0,n+1):
    print(res1(num1,i))
 



