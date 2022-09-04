#Q6]  Python Program to Sort Words in Alphabetic Order


ascending_order = lambda res1: sorted(res1)

str1 = input("Enter String : ")
str_lst = list(str1)
# print(str_lst)
res_lst = ascending_order(str_lst)
res_str = ''.join(res_lst)

print("Original String : {}".format(str1))
print("New String (in ascendning order) : {}".format(res_str))
 
# print("Ascending Order of the String : {}".format(res))