# Q8] Python Program to Make a Simple Calculator


plus = lambda x,y: x+y
minus = lambda x,y : x-y 
division = lambda x,y : x/y
multiplication = lambda x,y : x*y

print("Calculator:-")
print()

try_again = True
while(try_again):
    num1 = float(input("Enter Number 1 : "))
    num2 = float(input("Enter Number 2 : "))
    print("Operations :-")
    print()
    print("(1) Addition")
    print("(2) Subtraction")
    print("(3) Multiplication")
    print("(4) Division")
    print()
    user = int(input("Enter Serial Number : "))

    res = 0
    if(user == 1):
        res = plus(num1,num2)
    elif(user == 2):
        res = minus(num1,num2)
    elif(user == 3):
        res = multiplication(num1,num2)
    elif(user == 4):
        res = division(num1,num2)

    print("Result : {}".format(res))

    print()
    print("Press '0' to use the calculator again or '1' to stop")
    again = int(input("Enter : "))
    if(again == 0):
        try_again = True
    else:
        print("Thanks for using the calculator !!")
        try_again = False

    

