# Python Program to Check Armstrong Number


 


num = input("Enter number : ")

lst_num = list(num)

for i in range(0,len(lst_num)):
    lst_num[i] = int(lst_num[i])

 
add = 0
for i in lst_num:
    add += pow(i,len(lst_num))

if(add == int(num)):
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")


 