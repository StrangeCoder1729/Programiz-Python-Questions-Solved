# Q30] Python Program to Iterate Through Two Lists in Parallel

lst1 = list(map(int,input("Enter series of numbers for list 1 : ").split()))
lst2 = list(map(int,input("Enter series of numbers for list 2 : ").split()))


if (len(lst1) == len(lst2)):
    for i in range(0,len(lst1)):
        print(f"{lst1[i]} {lst2[i]}")