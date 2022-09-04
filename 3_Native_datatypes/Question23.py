#Q23]  Python Program to Randomly Select an Element From the List

import random as rand

def random_selection(temp_lst):
    rand_num = rand.randint(0,len(temp_lst))
    return temp_lst[rand_num]


lst = list(map(int, input("Enter series of the numbers : ").split()))
print()
print(lst)
print()
res = random_selection(lst)
print(res)