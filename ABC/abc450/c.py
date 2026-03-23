import sys

line1 = input().split()
H, W = map(int, line1)

S = [input() for _ in range(H)]

# 訪問済みマスの管理 (False=未訪問，True=訪問済み)
vis = [[False] * W for _ in range(H)]

ans = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for r in range(H):
    for c in range(W):
        if S[r][c] == '.' and not vis[r][c]:
            bn = False
            q = []
            q.append((r, c))
            vis[r][c] = True
            
            idx = 0
            
            while idx < len(q):
                cr, cc = q[idx]
                idx += 1
                
                if cr == 0 or cr == H - 1 or cc == 0 or cc == W - 1:
                    bn = True
                
                for k in range(4):
                    nr = cr + dr[k]
                    nc = cc + dc[k]
                    
                    if 0 <= nr < H and 0 <= nc < W:
                        if S[nr][nc] == '.' and not vis[nr][nc]:
                            vis[nr][nc] = True
                            q.append((nr, nc))
            
            if not bn:
                ans += 1
                
print(ans)
