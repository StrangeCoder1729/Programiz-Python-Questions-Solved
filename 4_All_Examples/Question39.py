#Q39] Python Program to Check Whether a String is Palindrome or Not

 


def check_Palindrome(temp_new_str1,temp_res):
    if(temp_new_str1 == temp_res):
        print("It is a Palindrome")
    else:
        print("It is not a Palindrome")

def reversing_string(temp_str1):
    new_str1 = temp_str1

    nth = len(temp_str1)-1
    i = 0
    res = ''
    while(nth >= i):
        res += str1[nth] 
        nth -=1
    check_Palindrome(new_str1,res)
    



str1 = input("Enter String : ")
reversing_string(str1)