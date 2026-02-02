n, t = map(int, input().split())

a = []
a = list(map(int, input().split()))

ans = 0 
cur = 0 
i = 0

while cur < t:
    while i < n and a[i] <= cur:
        i += 1

    if i == n:  
        ans += t - cur
        break

    nxt = a[i]
    ans += nxt - cur
    cur = nxt + 100 
    i += 1 

print(ans)
