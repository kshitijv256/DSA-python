import random as rd

def binSearch(arr,value,l,r):
    mid = (l+r)//2
    if arr[mid] == value:
        return mid
    elif arr[mid] < value:
        return binSearch(arr,value,mid+1,r)
    else:
        return binSearch(arr,value,l,mid-1)

arr = []
for i in range(20):
    arr.append(rd.randint(0,100))
arr.sort()
print(arr)
inp = int(input())

print(binSearch(arr,inp,0,19))