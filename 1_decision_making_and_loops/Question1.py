#Q1] Python Program to Check if a Number is Positive, Negative or 0


 


# from curses.ascii import isalpha


def detec(num):
    if(num == 0):
        print(num)
     
    elif(num > 0):
        print("{} is a Positive number".format(num))
    else:
        print("{} is a negative number".format(num))
 
    

num = input("Enter number : ")

num = int(num)
detec(num)









# if num.isalpha() == True:
#     print("It's a word")
# elif num.isnumeric() == True:
#     num = int(num)
#     detec(num)
# elif num.isalnum() == True:
#     print("This string contains both letters and numbers")
 

