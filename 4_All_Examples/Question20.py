#Q20 Python Program to Find Armstrong Number in an Interval


def armstrong(temp_num):

    temp_num = str(temp_num)
    temp_num1 = int(temp_num)
    temp_num = list(temp_num)
    add = 0
    for i in range(0,len(temp_num)):
        temp_num[i] = int(temp_num[i])
    for i in temp_num:
        add += pow(i,len(temp_num))
   

    if(add == temp_num1):
        return temp_num1
    
    


n1 = int(input("Enter lower limit : "))
n2 = int(input("Enter upper limit : "))

for i in range(n1,n2):
    if(armstrong(i) == None):
        continue
    print(armstrong(i))

 