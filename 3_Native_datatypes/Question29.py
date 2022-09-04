#Q29] Python Program to Trim Whitespace From a String

str1 = input("Enter String : ")

remove = ' '
result = ''
for element in str1:
    if(element not in remove):
        result += element

print(result)
