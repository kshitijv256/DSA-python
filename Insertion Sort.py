# Insertion Sort

from random import randint

def insSort(array):
    for i in range(1,len(array)):
        key =  array[i]
        j = i-1
        while j>=0 and key< array[j]:
            array[j+1] = array[j]
            j -=1
        array[j+1] = key
    return array

arr =[]
for i in range(30):
    arr.append(randint(0,100))
print(arr,'\n')
insSort(arr)
print(arr,'\n')