# Q5] Python Program to Remove Punctuations From a String

def removing_punctuation(temp_str,lst):
    # for i in range(0,len(temp_str)):
    result = ''
    for word in temp_str:
        if word not in lst:
            result += word
    return result
        



str1 = input("Enter String : ")
lst_punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
res = removing_punctuation(str1,lst_punctuations)

print("String with Punctuations : {}".format(str1))
print("String without Punctuations : {}".format(res))
 