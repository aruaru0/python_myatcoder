import sys
from collections import deque
H, W = map(int, input().split())
S = [input().strip() for _ in range(H)]

N = H * W
col = [0] * N          # 1: black , 0: white
used = [0] * N          # 隣接黒の個数 (白マスだけ使う)

def idx(i, j):
    return i * W + j

for i in range(H):
    row = S[i]
    for j, ch in enumerate(row):
        if ch == '#':
            col[idx(i, j)] = 1


# 隣接黒の個数を数える
dirs = [(1,0),(-1,0),(0,1),(0,-1)]

def calc(x, y) :
    c = 0
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= W or ny < 0 or ny >= H: 
            continue
        if col[idx(ny,nx)]:
            c += 1
    return c

que = []
for i in range(H):
    for j in range(W):
        id_ = idx(i, j)
        if col[id_] == 1:
            continue
        c = calc(j, i)
        if c == 1:
            que.append(id_)


while len(que) :
    for e in que:
        used[e] = 1
        col[e] = 1
    
    r = []
    for e in que:
        y, x = divmod(e, W)
        for dx, dy in dirs :
            nx, ny  = x + dx, y + dy
            if nx < 0 or nx >= W or ny < 0 or ny >= H: 
                continue
            if col[idx(ny,nx)]:
                continue
            c = calc(nx, ny)            
            if c == 1 :
                r.append(idx(ny, nx))    

    que = r


print(sum(col))            



