import sys
from collections import deque

h, w = map(int, input().split())
g = [input().strip() for _ in range(h)]

# warp lists for 'a' .. 'z'
mp = [[] for _ in range(26)]
for i in range(h):
    row = g[i]
    for j, ch in enumerate(row):
        if 'a' <= ch <= 'z':
            mp[ord(ch) - 97].append((i, j))

dist = [[-1] * w for _ in range(h)]
used = [False] * 26
dq = deque()
dq.append((0, 0))
dist[0][0] = 0

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while dq:
    x, y = dq.popleft()
    d = dist[x][y]
    if x == h-1 and y == w-1:
        print(d)
        exit()

    # walking
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and g[nx][ny] != '#' and dist[nx][ny] == -1:
            dist[nx][ny] = d + 1
            dq.append((nx, ny))

    # warp
    ch = g[x][y]
    if 'a' <= ch <= 'z':
        idx = ord(ch) - 97
        if not used[idx]:
            for nx, ny in mp[idx]:
                if dist[nx][ny] == -1:
                    dist[nx][ny] = d + 1
                    dq.append((nx, ny))
            used[idx] = True

print(-1)

