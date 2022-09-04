#Q6] Python Program to Swap Two Variables using third vairable


num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

print("Before Swapping :-")
print(f"Number 1 : {num1}")
print(f"Number 2 : {num2}")
print()
temp = 0
temp = num1
num1 = num2
num2 = temp

print("After Swapping :-")
print(f"Number 1 : {num1}")
print(f"Number 2 : {num2}")