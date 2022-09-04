#Q95] Python Program to Count the Number of Occurrence of a Character in String

str1 = input("Enter String : ")
str1 = str1.lower()
dict1 = {}

for letter in str1:dict1.update({letter:list(str1).count(letter)})
print(dict1)