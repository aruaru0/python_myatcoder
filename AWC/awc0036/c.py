n, k = map(int, input().split())

a = list(map(int, input().split()))

def check(m) :
    cnt, idx = 0,0
    while True :
        tot = 0
        while idx < n and tot+a[idx] <= m :
            tot += a[idx]
            idx += 1

        cnt += 1
        if idx == n : break

    if cnt > k+1 : return True
    return False

l = max(a)-1
r = sum(a)

while l+1 != r :
    m = (l+r)//2
    if check(m) == False :
        r = m
    else :
        l = m

print(r)