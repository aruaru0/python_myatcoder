n, k = map(int, input().split())

e = []
for i in range(n):
    l, r = map(int, input().split())
    e.append((l, 1))
    e.append((r, -1))

e.sort()

ans, cnt, prev = 0, 0, e[0][0]

for (x, val) in e :
    if cnt >= k :
        ans += x - prev
    cnt += val
    prev = x


print(ans)
