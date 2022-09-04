#Q4] Python Program to Check Leap Year

yr = int(input("Enter year : "))

if (yr % 4 == 0):
    if(yr % 100 == 0):
        if(yr % 400 == 0):
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")