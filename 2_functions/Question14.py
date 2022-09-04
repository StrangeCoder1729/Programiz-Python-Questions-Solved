# Q14] Python Program to Convert Decimal to Binary Using Recursion


def binary(dec):
    if dec > 1:
        binary(dec //2)
    print(dec % 2, end='')


deci = int(input("Enter Decimal : "))
binary(deci)