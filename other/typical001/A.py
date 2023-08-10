import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())

c = [input() for _ in range(H)]

sx, sy = 0,0
gx, gy = 0,0

for h in range(H):
    for w in range(W):
        if c[h][w] == 's' :
            sx, sy = w, h
        if c[h][w] == 'g' :
            gx, gy = w, h



dx = [-1, 1, 0, 0]
dy = [0 ,0 ,-1, 1]
def dfs(cx, cy) :
    used[cy][cx] = True
    for i in range(4):
        px = cx + dx[i]
        py = cy + dy[i]
        if px < 0 or px >= W or py < 0 or py >= H : continue
        if c[py][px] == '#' : continue
        if used[py][px] : continue
        dfs(px, py)

used = [[False for _ in range(W)] for _ in range(H)]
dfs(sx, sy)


if used[gy][gx] :
    print("Yes")
else :
    print("No")

 
