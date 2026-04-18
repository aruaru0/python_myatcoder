n, k = map(int, input().split())
a = list(map(int, input().split()))

tot = sum(a[:k])

ans = 0

if tot <= 0:
    ans += 1
    
for i in range(k, n):
    tot -= a[i-k]
    tot += a[i]
    if tot <= 0:
        ans += 1
        
print(ans)


