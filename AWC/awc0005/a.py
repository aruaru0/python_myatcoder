n, k = map(int, input().split())
p = list(map(int, input().split()))

ans = 0
for e in p :
    if e%k == 0 : ans += e

print(ans)