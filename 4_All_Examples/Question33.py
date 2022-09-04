#Q33]  Python Program to Find Sum of Natural Numbers Using Recursion

def summation(temp_n):
    if(temp_n == 1):
        return 1
    if(temp_n > 1):
        return temp_n + summation(temp_n-1)


n = int(input("Enter range : "))
print(summation(n))