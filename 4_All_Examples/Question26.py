# Q27] Python Program to Find HCF or GCD

def HCF(temp_num1,temp_num2):
    if(temp_num1 > temp_num2):
        smallest = temp_num2
    elif(temp_num1 < temp_num2):
        smallest = temp_num1
    else:
        smallest = temp_num1
    
    for i in range(2,smallest):
        if(temp_num1 % i == 0) and (temp_num2 % i == 0):
            hcf = i
            
    return hcf
    



num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

res = HCF(num1,num2)
print("HCF of {0} and {1} is {2}".format(num1,num2,res))