from collections import deque
import sys

H, W = map(int, input().split())
grid = [input() for _ in range(H)]

sr, sc = -1, -1
gr, gc = -1, -1
for r in range(H):
    for c in range(W):
        char = grid[r][c]
        if char == 'S':
            sr, sc = r, c
        elif char == 'G':
            gr, gc = r, c

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ch = ['U', 'D', 'L', 'R']

# pre[r][c][d]: マス(r, c)に方向dで入ってきたときの、1つ前のマスの方向
pre = [[[-1]*4 for _ in range(W)] for _ in range(H)]

q = deque()

# スタート地点の初期化
for i in range(4):
    pre[sr][sc][i] = 9
    q.append((sr, sc, i))

while q:
    r, c, d = q.popleft()
    
    # ゴールに到達した場合
    if r == gr and c == gc:
        ans = []
        while pre[r][c][d] != 9:
            ans.append(ch[d])
            # 前のマスと、そのマスでの向きに遡る
            r, c, d = r - dr[d], c - dc[d], pre[r][c][d]
        print("Yes") # Yesを出力
        print("".join(ans[::-1]))
        exit()
    
    cur = grid[r][c]
    
    # 現在のマスに応じた移動可能方向の決定
    if cur == 'o':
        moves = [d] # 直前と同じ方向のみ
    elif cur == 'x':
        moves = [i for i in range(4) if i != d] # 直前と違う方向のみ
    else:
        moves = [0, 1, 2, 3] # 全方向OK (. または S)
    
    for nd in moves:
        nr, nc = r + dr[nd], c + dc[nd]
        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != '#':
            if pre[nr][nc][nd] == -1:
                pre[nr][nc][nd] = d
                q.append((nr, nc, nd))

print("No")