# Q6] Python Program to Find LCM

def LCM(num1,num2):
    greatest = 0

    if(num1 > num2):
        greatest = num1
    else:
        greatest = num2
    
    while(True):
        if((greatest % num1 == 0) and (greatest % num2 == 0)):
            lcm = greatest
            break
        greatest += 1
    
    return greatest

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

res = LCM(num1,num2)
print("LCM of {0} and {1} : {2}".format(num1,num2,res))