# Q 15] Python Program to Reverse a Number


def reverse(num):
    temp = 0
    rev = 0
    while(num > 0):
        temp = num % 10
        rev = rev* 10 + temp
        num = num // 10
    return rev

num = int(input("Enter number : "))

print("Original number : {}".format(num))
res = 0
res = reverse(num)
print("Reverse number : {}".format(res))
