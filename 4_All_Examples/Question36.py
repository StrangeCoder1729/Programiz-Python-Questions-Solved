#Q36] Python Program to Add Two Matrices

def creating_matrix(temp_lst):
    temp_lst = []
    for i in range(0,3):
        temp_lst.append([])
        for j in range(0,3):
            user_input = int(input(f"Enter row {i} col {j} : "))
            temp_lst[i].append(user_input)
    return temp_lst

def showing_matrix(temp_lst1):
    for i in range(0,len(temp_lst1)):
        for j in range(0,len(temp_lst1[0])):
            print(temp_lst1[i][j],end=' ')
        print()

def matrix_zero(temp_mat):
    temp_mat =[]
    for i in range(0,3):
        temp_mat.append([])
        for j in range(0,3):
            temp_mat[i].append(0)
    return temp_mat
        

def addition_matrix(temp_res_mat,temp_mat1,temp_mat2):
    res_mat = matrix_zero(temp_res_mat)
    for i in range(0,len(temp_mat1)):
        for j in range(0,len(temp_mat1[0])):
            res_mat[i][j] = temp_mat1[i][j] + temp_mat2[i][j]
    return res_mat

def sol():
    lst1 = []
    print("For Matrix 1 :-")
    mat1 = creating_matrix(lst1)
    print()
    

    lst2 = []
    print("For Matrix 2 :-")
    mat2 = creating_matrix(lst2)
    print()

    print("Matrix 1 :-")
    showing_matrix(mat1)

    print()

    print("Matrix 2 :-")
    showing_matrix(mat2)

    
    mat3 = []

    print()
    mat_res = addition_matrix(mat3,mat1,mat2)
    # print(mat_res)
    print()
    print("Addition of Matrix 1 and Matrix 2")
    showing_matrix(mat_res)

sol()