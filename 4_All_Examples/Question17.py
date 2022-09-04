# Q17] Python Program to Display the multiplication Table

def multiplication(temp_num,n1,n2):
    
    mul = 1
    for i in range(n1,n2+1):
        mul = temp_num * i
        print(f"{temp_num} X {i} = {mul}")

num = int(input("Enter number : "))
n1 = int(input("Enter lower limit : "))
n2 = int(input("Enter upper limit : "))

multiplication(num,n1,n2)