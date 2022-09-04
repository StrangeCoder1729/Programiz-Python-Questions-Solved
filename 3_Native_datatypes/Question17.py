#Q17] Python Program to Split a List Into Evenly Sized Chunks

def spliting(temp_lst,temp_chunk):

    for i in range(0,len(temp_lst),chunk):
        yield (lst[i:i+chunk])
    


chunk = 2
lst = list(map(int, (input("Enter Series of numbers : ")).split()))
res = list(spliting(lst,chunk))
print(res)