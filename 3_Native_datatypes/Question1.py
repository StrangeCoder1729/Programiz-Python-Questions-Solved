# Q1] Python Program to Add Two Matrices

def matrix_formation(temp_matrix):
    temp_matrix = []
    for i in range(0,3):
        temp_matrix.append([])
        for j in range(0,3):
            user_input = int(input(f"Row {i} Column {j} : "))
            temp_matrix[i].append(user_input)
    return temp_matrix

    
matrix1 = []
matrix2 = []
res1 = matrix_formation(matrix1)
print()
res2 = matrix_formation(matrix2)

 
matrix3 = []
for i in range(0,len(res1)):
    matrix3.append([])
    for j in range(0,len(res1[0])):
        automate = 0
        matrix3[i].append(automate)
print(matrix3)


for i in range(0,len(res1)):
    for j in range(0,len(res1[0])):
        matrix3[i][j] = res1[i][j] + res2[i][j]

print(matrix3)



 


 
