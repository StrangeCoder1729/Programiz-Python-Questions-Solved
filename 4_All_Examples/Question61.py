#Q61] Python Program to Parse a String to a Float or Int
try: 
    str1 = input("Enter String : ")
    
    if str1.isnumeric() == True:
        int_str1 = int(str1)
        print(f"{str1} is numeric")
        print(f"Parsing String to integer : {int_str1}")

    
    elif str1.isalpha() == True:
        alpha_str1 = str(str1)
        print(f"{str1} is string")
        print(f"Parsing String to integer : {alpha_str1}")

    elif '.' in str1:
        float_str1 = float(str1)
        print(f"{str1} is decimal")
        print(f"Parsing String to float : {float_str1}")

    else:
        print("Other...")
except Exception as E:
    print("Invalid input !!")