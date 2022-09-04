#Q24]  Python Program to Check If a String Is a Number (Float)


def detec(temp_str1):
    if temp_str1.isnumeric() == True:
        print("Not a Float Number")
    elif temp_str1.isalpha() == True or " " in temp_str1:
        print("Not a Float number")
    elif '.' in temp_str1 and " "not in temp_str1:
        temp_str1_float = float(temp_str1)
        print("It is a Float number")
        # if temp_str1.isalpha() == False :
        #     print("It is a Float number")
    else:
        print("Others...")
    


str1 = input("Enter String : ")
detec(str1)

