#Q91] Python Program to Count the Number of Digits Present In a Number


num = int(input("Enter numeber : "))
temp = num
counting = 0
while(num >0):
    num = num// 10
    counting +=1

print("Number of digits in {0} is {1}".format(temp,counting))
