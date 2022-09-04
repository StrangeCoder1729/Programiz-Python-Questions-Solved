# Q3] Python Program to Find the Square Root

def sqroot(num):
    sol = pow(num,0.5)
    return round(sol,3)

num = int(input("Enter the number : "))

res = sqroot(num)
print("The Square root of {0} is {1}".format(num,res))