# Python Program to Convert Kilometers to Miles


miles = lambda x:round (x*0.62137119,3)

num = float(input("Enter number : "))

res = miles(num)
print("Miles : {}".format(res))