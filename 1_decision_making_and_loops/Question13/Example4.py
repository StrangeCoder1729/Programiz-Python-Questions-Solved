# Example 4: Inverted half pyramid using *

"""
n = 5
* * * * * 
* * * *
* * *
* *
*
"""
n = int(input("Enter number of rows : "))

for i in range(0,n):
    for j in range(0,n-i):
        print("*",end=' ')
    print()
