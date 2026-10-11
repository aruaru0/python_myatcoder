n, r = map(int, input().split())

cnt = 0
for _ in range(n) :
    x0, y1, x1, y2 = map(int, input().split())
    dx, dy = x1 - x0, y2 - y1
    if dx*dx + dy*dy <= r*r :
        cnt+=1

print(cnt)