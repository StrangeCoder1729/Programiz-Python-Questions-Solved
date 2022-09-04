# Q29] Python Program to Make a Simple Calculator

add = lambda x,y : x+y
sub = lambda x,y : x-y
div = lambda x,y : x/y
mul = lambda x,y : x*y
remain = lambda x,y  : x%y

num1 = float(input("Enter Number 1 : "))
num2 = float(input("Enter Number 2 : "))
print("Operators:-")
print("+, -, / , x, %")
op = input("Choose an operator : ")
if(op == '+'): print(add(num1,num2))
elif(op == '-'): print(sub(num1,num2))
elif(op == '/'): print(div(num1,num2))
elif(op == 'x'): print(mul(num1,num2))
elif(op == '%'): print(remain(num1,num2))

