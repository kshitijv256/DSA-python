import random as rd

def minMax(arr):
    min = 1000
    max = 0
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        minMax(left)
        minMax(right)
        
        i=j=k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                if min > left[i]:
                    min = left[i]
                if max < right[j]:
                    max = right[j]
                i += 1
            else:
                if max < left[i]:
                    max = left[i]
                if min > right[j]:
                    min = right[j]
                j += 1
            k += 1

        while i < len(left):
            if max < left[i]:
                max = left[i]
            elif min > left[i]:
                min = left[i]
            i += 1
            k += 1
  
        while j < len(right):
            if max < right[j] :
                max = right[j]
            elif min > right[j]:
                min = right[j]
            j += 1
            k += 1
    return min,max
        
def minMax_old(arr):
    min = 1000
    max = 0
    for i in arr:
        if min > i:
            min = i
        elif max < i:
            max = i
    return min,max


li = []
for i in range(8000000):
    li.append(rd.randint(0,100))

#print(li)
print(minMax_old(li))
