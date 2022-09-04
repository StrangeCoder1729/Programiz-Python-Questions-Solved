# Q10] Python Program to Check Armstrong Number


def detec(num,res):
    
    if (num == res):
        print("It is an Armstrong number")
    else:
        print("It is not an Armstrong number")


def armstrong(num):
    num1 = num
    temp = 0
    rev = 0
    add = 0
    num_count = len(str(num1))
    while(num > 0):
        temp = num % 10
        # rev = rev*10 + temp 
        add = add + pow(temp,num_count)
        num = num // 10
    return add



num = int(input("Enter number : "))

res = 0
res = armstrong(num)
detec(num,res)