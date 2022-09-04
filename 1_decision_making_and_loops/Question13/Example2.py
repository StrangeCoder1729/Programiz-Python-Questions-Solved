# Example 2: Program to print half pyramid a using numbers

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5 
n = 6
"""
n = int(input("Enter number of rows : "))

for i in range(0,n):
    for j in range(0,i):
        print(j+1,end =' ')
    print()