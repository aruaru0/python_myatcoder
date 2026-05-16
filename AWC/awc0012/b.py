n, T, C, D = map(int, input().split())
Ws = list(map(int, input().split()))
ans = 0
for w in Ws:
    if w >= T:
        ans += min(C, D)
print(ans)