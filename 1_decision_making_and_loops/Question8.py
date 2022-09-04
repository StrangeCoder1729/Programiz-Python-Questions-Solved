# Q8] Python Program to Display the multiplication Table



def mul(num,n):
    multi = 1
    for i in range(1,n+1):
        multi = num*i
        print(f"{num} X {i} = {multi}")



num = int(input("Enter number : "))
n = int(input("Enter range : "))


mul(num,n)