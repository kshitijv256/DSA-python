import random

def swap(a,b):
    return b,a

def quick(arr,l,r):
    if l<r:
        index = part(arr,l,r)
        quick(arr,l,index-1)
        quick(arr,index+1,r)

def part(arr,l,r):
    index = r 
    store = l-1
    for i in range(l,r):
        if arr[i] <= arr[index]:
            store += 1
            arr[i],arr[store] = swap(arr[i],arr[store])
    arr[index],arr[store+1] =swap(arr[index],arr[store+1])
    return store+1

n = int(input("\nEnter length of required Array:\n"))
li = []
for i in range(n):
    li.append(random.randint(0,100))
print('\nUnsorted Array:\n',li)
quick(li,0,n-1)
print('\nSorted Array:\n',li)