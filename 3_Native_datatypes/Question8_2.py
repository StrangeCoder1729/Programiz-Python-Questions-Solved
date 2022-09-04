# Q8] Python Program to Count the Number of Each Vowel

def vowels(temp_str,all_vows):
    dict = {}
    for letter in temp_str:
        if letter in all_vows:
            counting = temp_str.count(letter)
            dict.update({letter:counting})
    return dict




str1 = input("Enter String : ")
str_vow = 'aeiou'
res = vowels(str1,str_vow)

print(res)