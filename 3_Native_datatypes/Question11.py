# Q11] Python Program to Flatten a Nested List

lst = []

for i in range(0,3):
    lst.append([])
    for j in range(0,3):
        user_input = int(input(f"Enter row {i} Column {j} : "))
        lst[i].append(user_input)

print(lst)

lst2 = []

print()
print("Nested Loop :-")
for i in range(0,len(lst)):
    for j in range(0,len(lst[0])):
        print(lst[i][j],end =' ')
    print()


for i in range(0,len(lst)):
    for j in range(0,len(lst)):
        lst2.append(lst[i][j])

print()
print("Flattened List:-")
print(lst2)