#Q9] Python Program to Convert Celsius To Fahrenheit


def Fahrenheit(c):
    f = ((9*c)/5)+32
    return f


num = float(input("Enter Celsius : "))

res = Fahrenheit(num)
print("Fahrenheit : {}".format(res))