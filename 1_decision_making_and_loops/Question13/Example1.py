# Example 1: Program to print half pyramid using *
"""
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * * 
 n = 10
"""

n = int(input("Enter rows : "))

for i in range(0,n):
    for j in range(0,i):
        print("*",end=' ')
    print()