# 92] Python Program to Check If Two Strings are Anagram


str1 = input("Enter String 1 : ")
str2 = input("Enter String 2 : ")

lst_str1 = list(str1)
lst_str2 = list(str2)

lst_str1.sort()
lst_str2.sort()
 
if(lst_str1 == lst_str2):print("Its an Anagram")
else:print("Not an Anagram")
