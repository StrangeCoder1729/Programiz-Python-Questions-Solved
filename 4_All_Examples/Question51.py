#Q51] Python Program to Flatten a Nested List

def flattening_list(temp_flat_lst):
    new_lst = []
    for i in range(0,len(temp_flat_lst)):
        for j in range(0,len(temp_flat_lst[0])):
            new_lst.append(temp_flat_lst[i][j])
    return new_lst



def creation_nested_list(temp_lst):
    temp_lst =[]
    for i in range(0,3):
        temp_lst.append([])
        for j in range(0,3):
            user_input = int(input(f"Enter row {i} col {j} : "))
            temp_lst[i].append(user_input) 
    
    return temp_lst


lst = []
ns_lst = creation_nested_list(lst)

print("Nested list : {}".format(ns_lst))
print()
ns_lst_flat = flattening_list(ns_lst)
print("Flattening List : {}".format(ns_lst_flat))