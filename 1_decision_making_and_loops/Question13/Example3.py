# Example 3: Program to print half pyramid using alphabets
"""
n = 5

A       
B B     
C C C   
D D D D 
"""
n = int(input("Enter number of rows : "))

alpha = 64
for i in range(0,n):
    for j in range(0,i):
        alph = chr(alpha)
        print(alph,end =' ')
    alpha +=1
    print()