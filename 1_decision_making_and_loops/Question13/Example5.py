# Example 5: Inverted half pyramid using numbers
"""
n = 5
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1
"""
n = int(input("Enter number of rows : "))

for i in range(0,n):
    for j in range(0,n-i):
        print(j+1,end=' ')
    print()