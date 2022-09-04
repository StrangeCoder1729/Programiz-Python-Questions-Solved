# Q90] Python Program to Compute the Power of a Number

power = lambda x,y: round(pow(x,y),2)


num = float(input("Enter number : "))
num_pow = float(input("Enter power : "))

res = power(num,num_pow)
print(res)