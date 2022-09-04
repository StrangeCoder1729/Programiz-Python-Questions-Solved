#Q64] Python Program to Get the Last Element of the List

lst_num = list(map(int,input("Enter series of numbers : ").split()))

last_element = lst_num[len(lst_num)-1]

print("Last Element of the list is {}".format(last_element))