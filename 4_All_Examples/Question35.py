#Q35] Python Program to Convert Decimal to Binary Using Recursion

def bin_to_deci(temp_deci):
    if(temp_deci > 1):
        bin_to_deci(temp_deci//2)
    print(temp_deci % 2, end ='')


deci = int(input("Enter Decimal : "))
bin_to_deci(deci)