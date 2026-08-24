n, m, k = map(int, input().split())
a = list(map(int, input().split()))


l, tot = 0,0
eat = []

for r in range(n) :
    if r-l >= m :
        if eat[l] : tot -= a[l]
        l+=1
    if tot+a[r] <= k :
        tot += a[r]
        eat.append(True)
    else:
        eat.append(False)


print(*["Yes" if e else "No" for e in eat], sep="\n")