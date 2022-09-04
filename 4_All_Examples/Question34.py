#Q34] Python Program to Find Factorial of Number Using Recursion

def fact(temp_num):
    if(temp_num == 0) or (temp_num == 1):
        return 1
    else:
        return temp_num*fact(temp_num-1)



num = int(input("Enter number to find the factorial : "))

print(fact(num))