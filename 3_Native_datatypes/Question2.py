#Q2] Python Program to Transpose a Matrix


"""Function to construct a matrix"""
def matrix_transformation(temp_matrix):
    for i in range(0,3):
        temp_matrix.append([])
        for j in range(0,3):
            user_input = int(input(f"Enter Row {i} Column {j} : "))
            temp_matrix[i].append(user_input)
    return temp_matrix

matrix1 = []
matrix2 = []

print("Matrix 1 :-")

"""Creating a Matrix"""
res1 = matrix_transformation(matrix1)
 
# print("Matrix 1 :-")
# print(res1)
 
matrix2 = []

"""Creating Matrix 2 and Inputting the values of Matrix 2 as Zeros"""
for i in range(0,len(res1)):
    matrix2.append([])
    for j in range(0,len(res1[0])):
        automate = 0
        matrix2[i].append(0)

"""Transforming Matrix 1 into a transpose form ans storing it in matrix 2"""
for i in range(0,len(res1)):
    for j in range(0,len(res1[0])):
        matrix2[i][j] = res1[j][i] 

print("Matrix 1 :-")
for i in range(0,len(res1)):
    for j in range(0,len(res1[0])):
        print(res1[i][j],end=' ')
    print()

print("Matrix 1 (Transpose):-")
for i in range(0,len(res1)):
    for j in range(0,len(res1[0])):
        print(matrix2[i][j],end=' ')
    print()