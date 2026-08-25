from collections import deque

h, w, k = map(int, input().split())
s = [input() for _ in range(h)]

cnt_h = [0]*h
cnt_w = [0]*w
for r in range(h):
    for c in range(w):
        if s[r][c] == '#' : 
            cnt_h[r]+=1
            cnt_w[c]+=1

inf = 1e18
dist =[[inf for _ in range (w)] for _ in range (h)]
q = deque()
for r in range(h):
    for c in range(w):
        if cnt_h[r] == 0 and cnt_w[c] == 0 :
            q.append((r, c))
            dist[r][c] = 0


dr = [-1, 1, 0 , 0]
dc = [0, 0, -1, 1]

while len(q) != 0 :
    cr, cc = q[0]
    q.popleft()
    for i in range(4):
        nr, nc = cr + dr[i], cc + dc[i]
        if nr < 0 or nr >= h or nc < 0 or nc >= w : continue
        if s[nr][nc] == '#' : continue
        if dist[nr][nc] != inf : continue
        q.append((nr, nc))
        dist[nr][nc] = dist[cr][cc] + 1


ans = 0
for r in range(h):
    for c in range(w) :
        if dist[r][c] <= k : ans+=1

print(ans)
