# Q22] Python Program to Display Powers of 2 Using Anonymous Function

powers_2 = lambda x : pow(x,2)

n = int(input("Enter n : "))
for i in range(0,n):
    print(powers_2(i))