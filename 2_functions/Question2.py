# Q2] Python Program to Find Numbers Divisible by Another Number


def divisibility(num1,num2):
    res = 0
    if(num1 > num2):
        res = num1 % num2
    elif(num1 < num2):
        res = num2 % num1
    elif(num1 == num2):
        res = 0
    
    return res

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

sol = divisibility(num1,num2)
print("Answer : {}".format(sol))



