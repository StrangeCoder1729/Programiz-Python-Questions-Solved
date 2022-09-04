# Q75] Python Program to Measure the Elapsed Time in Python

import time
 
start = time.time()
num1 = float(input("Enter number 1 : "))
num2 = float(input("Enter number 2: "))
print(num1*num2)
end = time.time()

print(f"{start} - {end}")