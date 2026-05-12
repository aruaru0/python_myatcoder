n, k = map(int, input().split())
a = list(map(int, input().split()))

def f(m) :
    tot = 0
    for i in range(n) :
        cnt = max(0, (m-a[i]+i)//(i+1))
        tot += cnt
    return tot

l, r = 0, 10**19
while l + 1 != r :
    m = (l+r)//2
    if f(m) > k :
        r = m
    else :
        l = m

print(l)