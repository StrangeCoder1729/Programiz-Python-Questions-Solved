#Q16] Python Program to Find the Factorial of a Number

def fact(temp_num):
    fact_num = temp_num
    for i in  range(1,temp_num):
        fact_num *= i
    return fact_num




num = int(input("Enter number : "))
print(fact(num))