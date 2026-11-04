import sys
from collections import deque


def bfs(s, ban):
    dist = [-1] * n
    par = [-1] * n
    dist[s] = 0
    dq = deque([s])
    while dq:
        x = dq.popleft()
        for y in g[x]:
            if y == ban or dist[y] != -1:
                continue
            dist[y] = dist[x] + 1
            par[y] = x
            dq.append(y)
    return dist, par


n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
C = list(map(int, input().split()))

# 直径の端点 A, B と直径 D を求める
dist0, _ = bfs(0, -1)
A = max(range(n), key=lambda i: dist0[i])
distA, parA = bfs(A, -1)
B = max(range(n), key=lambda i: distA[i])
D = distA[B]

# A から B へのパス（直径パス）
path = []
x = B
while True:
    path.append(x)
    if x == A:
        break
    x = parA[x]
path.reverse()

if D % 2 == 0:
    # 中心は頂点 c, D = 2R
    R = D // 2
    c = path[R]
    dist = [-1] * n
    br = [-1] * n
    dist[c] = 0
    dq = deque()
    for y in g[c]:
        dist[y] = 1
        br[y] = y
        dq.append(y)
    while dq:
        x = dq.popleft()
        for y in g[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                br[y] = br[x]
                dq.append(y)

    tot = {}
    per = {}
    for v in range(n):
        if dist[v] == R:
            col = C[v]
            tot[col] = tot.get(col, 0) + 1
            key = (br[v], col)
            per[key] = per.get(key, 0) + 1

    ans = 0
    for x in tot.values():
        ans += x * (x - 1) // 2
    for x in per.values():
        ans -= x * (x - 1) // 2
    print(ans)
else:
    # 中心は辺 (c1, c2), D = 2R+1
    R = D // 2
    c1 = path[R]
    c2 = path[R + 1]
    d1, _ = bfs(c1, c2)
    d2, _ = bfs(c2, c1)

    cnt1 = {}
    cnt2 = {}
    for v in range(n):
        if d1[v] == R:
            col = C[v]
            cnt1[col] = cnt1.get(col, 0) + 1
        if d2[v] == R:
            col = C[v]
            cnt2[col] = cnt2.get(col, 0) + 1

    ans = 0
    for col, x in cnt1.items():
        ans += x * cnt2.get(col, 0)
    print(ans)
