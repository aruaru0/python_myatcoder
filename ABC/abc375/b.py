import math

n = int(input())

xy = [list(map(int, input().split())) for _ in range(n)]
xy.append([0,0])

cx, cy = 0,0
ans = 0.0
for x, y in xy :
    dx = x - cx
    dy = y - cy
    ans += math.sqrt(dx*dx + dy*dy)
    cx, cy = x, y

print(ans)