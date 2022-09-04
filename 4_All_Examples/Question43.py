#Q43]  Python Program to Count the Number of Each Vowel

vowels = "aeiou"

str1 = input("Enter String : ")
str1 = str1.lower()

res = ""
for i in range(0,len(str1)):
    if str1[i] in vowels:
        res += str1[i]

total_no_of_vowels = len(res)
print("Total number of vowels in {0} is/are {1}".format(str1,total_no_of_vowels))
