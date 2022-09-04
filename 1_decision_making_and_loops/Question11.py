 

def armstrong(num):
    num1 = num
    temp = 0
    rev = 0
    add = 0
    num_count = len(str(num1))
    while(num > 0):
        temp = num % 10
        # rev = rev*10 + temp 
        add = add + pow(temp,num_count)
        num = num // 10
    
    if(num1 == add):
        return num1




n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))

for i in range(n1,n2):
    if(armstrong(i) == None):
        continue
    print(armstrong(i),end = ' ')
 