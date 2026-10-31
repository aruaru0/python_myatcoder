n = int(input())

p = [(r, l) for l, r in [map(int, input().split()) for i in range(n)]]

p.sort()

ans = 0
cur = 0
for i in range(n):
    r, l = p[i]
    if l >= cur :
        cur = r
        ans += 1

print(ans)
