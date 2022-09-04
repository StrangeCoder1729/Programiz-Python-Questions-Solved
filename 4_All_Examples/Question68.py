#Q68] Python Program to Randomly Select an Element From the List

import random as rand
lst = list(map(int,input("Enter series of numbers : ").split()))


rand_index = rand.randint(0,len(lst)-1)

print(lst[rand_index])
