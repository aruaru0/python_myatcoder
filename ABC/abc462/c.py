n = int(input())
pts = [tuple(map(int, input().split())) for _ in range(n)]
pts.sort(key=lambda p: p[0])

min_y = float('inf')
ans = 0
for x, y in pts:
    if y < min_y:
        ans += 1
        min_y = y

print(ans)
