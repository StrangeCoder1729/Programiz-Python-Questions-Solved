# Q32] Python Program to Check If Two Strings are Anagram

str1 =  input("Enter String 1 : ")
lst_str1 = list(str1)

str2 = input("Enter String 2 : ")
lst_str2 = list(str2)

if(sorted(lst_str1) == sorted(lst_str2)):
    print("The two strings are Anagram")