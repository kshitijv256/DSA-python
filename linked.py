n = int(input())
li = list(map(int,input().split()))

def maxCount(li):
    mx = (0,0)
    counter = {}
    for i in li:
        if i not in counter:
            counter[i] = 0
        else:
            counter[i]+=1
            if counter[i] == mx[1]:
                mx = max(i,mx)
            elif counter[i]>mx[1]:
                mx[1] = counter[i]
                mx[0] = i
    return mx
                   