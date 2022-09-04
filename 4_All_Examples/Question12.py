# Q12] Python Program to Check Leap Year


yr = int(input("Enter year : "))

if(yr % 4 == 0):
    if(yr % 100 == 0):
        if(yr % 400 == 0):
            print("Its a Leap Year")
    else:
        print("Its a Leap Year")
else:
    print("Not a Leap Year")