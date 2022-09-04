#Q55] Python Program to Check If a List is Empty

lst = []

len_lst = len(lst)
# print(len_lst)
if len_lst == 0:
    print("Empty List")
elif [] in lst:
    if(len_lst == 1):
        print("Its an empty nested list ")
    else:
        print("Not an empty nested list")
else:
    print("Not a empty list")