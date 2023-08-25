x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

if r1 > r2 :
    r1, r2 = r2, r1

dx = x1 - x2
dy = y1 - y2
r = dx*dx + dy*dy
dm = r1 - r2
dp = r1 + r2
dm *= dm
dp *= dp

ans = 0
if dm > r : ans = 1
elif r == dm : ans = 2
elif dp == r : ans = 4
elif r > dp : ans = 5
else: ans = 3

print(ans)
