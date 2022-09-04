#Q4]  Python Program to Check Whether a String is Palindrome or Not


def reverse_string(temp_str):
    i = len(temp_str)-1
    res = ''
    while(i >= 0):
        user = temp_str[i]
        res += user
        i-=1
    return res

def checking_palindrome(original_str,reverse_str):
    if(original_str == reverse_str):
        print(f"{original_str} is a Palindrome")
    else:
        print(f"{original_str} is not a Palindrome")
str1 = input("Enter String : ")
str_reverse = reverse_string(str1)
checking_palindrome(str1,str_reverse)

 

