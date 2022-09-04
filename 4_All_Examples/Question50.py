#Q50] Python Program to Access Index of a List Using for Loop

def give_index(temp_lst,temp_user_num):
    k = 0
    for i in temp_lst:
        if i == temp_user_num:
            return k
        k+=1
         

lst_num = list(map(int,(input("Enter series of numbers : ").split())))

print(lst_num)
user_num = int(input("Which index of number you want to know : "))
print(give_index(lst_num,user_num))

