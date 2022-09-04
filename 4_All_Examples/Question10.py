#Q10] Python Program to Check if a Number is Positive, Negative or 0


def detect(num):
    if(num > 0):
        print("Number is Positive")
    elif(num < 0):
        print("Number is Negative")
    else:
        print("Number is Zero")
num = int(input("Enter number : "))
detect(num)