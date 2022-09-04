#Q40] Python Program to Remove Punctuations From a String


def remove_punc(temp_punc,temp_str1):
    i = 0
    nth = len(temp_str1)-1
    res = ''
    while(i <= nth):
        if temp_str1[i] not in temp_punc:
            res += temp_str1[i]
        i+=1
    return res
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

str1 = input("Enter string : ")

print(remove_punc(punctuations,str1))