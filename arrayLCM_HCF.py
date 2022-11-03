def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a,b):
    return a*b//gcd(a,b)

def getTotalX(a,b):
    a_lcm = a[0]
    for i in range(1,len(a)):
        a_lcm = lcm(a_lcm,a[i])

    b_hcf = b[0]
    for i in range(1,len(b)):
        b_hcf = gcd(b_hcf,b[i])

    count = 0
    for i in range(a_lcm,b_hcf+1,a_lcm):
        if b_hcf%i == 0:
            count+=1
    return count

## Test
a=[2,4]
b=[16,32,96]

print(getTotalX(a,b))