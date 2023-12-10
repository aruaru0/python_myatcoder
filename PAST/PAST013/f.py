import math

N = int(input())
a,b,c,d = map(int, input().split())
x = input()

x = int(x[0]+x[2:])

tot = (a + b*2 + c*3 + d*4)*1000

l, r = -1, 10**18
while l + 1 != r :
    m = (l+r)//2
    if tot + m*1000 <= x * (N+m) :
        r = m
    else :
        l = m

print(r)
