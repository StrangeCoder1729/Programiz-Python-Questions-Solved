#Q27] Python Program to Find LCM

def LCM(temp_num1,temp_num2):
    if(temp_num1 > temp_num2):
        greatest = temp_num1
    elif(temp_num2 > temp_num1):
        greatest = temp_num2
    else:
        greatest = temp_num1
    while(True):
        if(greatest % temp_num1== 0) and (greatest % temp_num2 == 0):
            return greatest
             
        greatest +=1
    
        

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

res = LCM(num1,num2)
print("LCM of {0} and {1} is {2}".format(num1,num2,res))