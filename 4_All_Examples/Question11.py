#Q11] Python Program to Check if a Number is Odd or Even

def detec(num):
    if(num % 2 == 0):
        print("Number is Even")
    elif(num % 2 == 1):
        print("Number is Odd")


num = int(input("Enter number : "))
detec(num)