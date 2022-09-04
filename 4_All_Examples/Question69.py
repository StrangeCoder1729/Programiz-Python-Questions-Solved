#Q69] Python Program to Check If a String Is a Number (Float)


try : 
    num = input("Enter number : ")
    num = float(num)

    print("{} is decimal".format(num))


except Exception as e:
    print("Not a decimal number")