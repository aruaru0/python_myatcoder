from sortedcontainers import SortedSet

H, W = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [ 0, 0,-1, 1]
m = SortedSet()
for h in range (H) :
    for w in range(W):
        for i in range(4):
            px = w + dx[i]
            py = h + dy[i]
            if px < 0 or px >= W or py < 0 or py >= H :
                continue
            x = a[h][w]
            y = a[py][px]
            if x > y :
                x, y = y , x
            m.add((x, y))

for e in m :
    print(e[0], e[1])