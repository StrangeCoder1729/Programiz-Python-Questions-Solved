#Q89] Python Program to Reverse a Number

def revers(temp_num):
    # copy_temp_num = temp_num
    last_digit = 0
    rev = 0
    while(temp_num > 0):
        last_digit = temp_num % 10
        rev  = rev* 10 + last_digit 
        temp_num  = temp_num // 10

    return rev

        


num = int(input("Enter number : "))
reverse_num = revers(num)
print("After Reverse function:-")
print(reverse_num)

