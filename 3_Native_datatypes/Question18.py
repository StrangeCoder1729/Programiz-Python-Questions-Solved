#Q18} Python Program to Parse a String to a Float or Int



num = input("Enter String containing a number : ")

if num.isnumeric() == True:
    res = int(num)
    print("Integer number : {}".format(res))

elif num.isalpha() == True:
    print("It is a String")
else:
    res = float(num)
    print("Decimal number : {}".format(res))
# elif num.isdecimal() == True:
#     res = float(num)
#     print("Decimal number : {}".format(res))