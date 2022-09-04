# Q60] Python Program to Split a List Into Evenly Sized Chunks

def split(temp_lst,temp_chunk):
    for i in range(0,len(temp_lst),temp_chunk):
        yield temp_lst[i:i + temp_chunk]

    


chunk = 5
lst = list(map(int,input("Enter Series of numbers : ").split()))
print(list(split(lst,chunk)))
