#Q41] Python Program to Sort Words in Alphabetic Order

str1 = input("Enter String : ")

lst_str1 = list(str1)

sorted_lst_str1 = sorted(lst_str1)

sorted_str1 = ''.join(sorted_lst_str1)

print("New String : {}".format(sorted_str1))