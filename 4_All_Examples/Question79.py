# Q79] Python Program to Trim Whitespace From a String

str1 = input("Enter String : ")

res = ' '
res1 = res
for i in str1:
    if i is res:
        continue
    res1+=i
  

print(res1)

        
