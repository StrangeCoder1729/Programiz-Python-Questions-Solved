#Q35] Python Program to Count the Number of Occurrence of a Character in String

str1 = input("Enter String : ")

dict1 = {}
for i in range(0,len(str1)):
    counting = str1.count(str1[i])
    dict1.update({str1[i]:counting})

print(dict1)