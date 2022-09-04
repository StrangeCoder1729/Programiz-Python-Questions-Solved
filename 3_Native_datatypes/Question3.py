# Q3] Python Program to Multiply Two Matrices

"""Constructing a Matrix"""
def matrix_transformation(temp_matrix):
    for i in range(0,3):
        temp_matrix.append([])
        for j in range(0,3):
            user_input = int(input(f"Enter Row {i} Column {j} : "))
            temp_matrix[i].append(user_input)
    return temp_matrix


"""Constructing a Skeleton of Matrix where the all the inputs are Zeros"""
def matrix_skelton(temp_matrix):
    for i in range(0,3):
        temp_matrix.append([])
        for j in range(0,3):
            automate = 0
            temp_matrix[i].append(automate)
    return temp_matrix

"""Multiplication Matrix Function"""
def matrix_multiplication(m1,m2,res):
    for i in range(0,len(m1)):
        for j in range(0,len(m1[0])):
            for k in range(0,len(m1)):
                res[i][j] += m1[i][k] * m2[k][j]
         
    return res

matrix1 = []
matrix2 = []

print("Matrix 1 :- ")
res1 = matrix_transformation(matrix1)
print()
print("Matrix 2:- ")
res2 = matrix_transformation(matrix2)


matrix3 = []
res3 = matrix_skelton(matrix3)


ans = matrix_multiplication(res1,res2,res3)
print(ans)





