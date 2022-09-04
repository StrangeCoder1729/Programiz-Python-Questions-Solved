# Example 6: Program to print full pyramid using *
"""
n = 5
    *
   * *
  * * *
 * * * *
"""
n = int(input("Enter number of rows : "))
 
for i in range(0,n):
    for j in range(i,n):
        print(" ",end ='')
    for k in range(0,i):
        print("* ",end='')
    print()
    
