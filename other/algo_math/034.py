n = int(input())

xy = [list(map(int, input().split())) for _ in range(n)]

ans = 1e18
for i in range(n):
    for j in range(i+1, n):
        x0, y0 = xy[i]
        x1, y1 = xy[j]
        d = (x0-x1)**2 + (y0-y1)**2
        ans = min(ans, d)

print(ans**0.5)

