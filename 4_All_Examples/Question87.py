#Q87] Python Program to Iterate Through Two Lists in Parallel

lst1 = list(map(int,input("Enter Series of numbers in list 1 : ").split()))
lst2 = [num for num in input("Enter Elements for list 2 : ").split()]



for i in range (min(len(lst1),len(lst2))):
    print(lst1[i],lst2[i])
