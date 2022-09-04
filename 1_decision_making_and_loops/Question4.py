#Q4] Python Program to Find the Largest Among Three Numbers


def maximum(lst):
    maxi = max(lst)
    return maxi
lst = []

n = int(input("Enter n : "))

for i in range(0,n):
    user_input = int(input("Enter number {}: ".format(i+1)))
    lst.append(user_input)

res = maximum(lst)
print("Maximum number is {}".format(res))