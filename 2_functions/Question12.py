#Q12] Python Program to Find Sum of Natural Numbers Using Recursion

def summation(num):
    if(num > 0):
        return num + summation(num-1)
    else:
        return 0
    



n = int(input("Enter n : "))

print(summation(n))
