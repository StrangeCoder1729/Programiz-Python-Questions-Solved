#] Python Program to Count the total number of vowels in the string


def vowels(temp_str,all_vowels):
    res = ''
    for letter in temp_str:
        if letter in all_vowels:
            res += letter
    return res


str1 = input("Enter String : ")
all_vowels = 'aeiou'
str_res = vowels(str1,all_vowels)
counting = len(str_res)
print("Number of vowels present in {0} is {1}".format(str1,counting))