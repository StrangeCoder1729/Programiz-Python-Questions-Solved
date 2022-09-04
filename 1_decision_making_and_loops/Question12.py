#Q12] Python Program to Find the Sum of Natural Numbers



n1 = int(input("Enter range 1 : "))
n2 = int(input("Enter range 2 : "))

if(n1 < 0 or n2 < 0):
    print("Cant accept negative values")
    exit()
if(n1 > n2):
    temp = 0
    temp = n1 
    n1 = n2
    n2 = temp
add = 0
for i in range(n1,n2+1):
    add +=i

print("Sum of the Natural numbers from {0} to {1} is {2}".format(n1,n2,add))