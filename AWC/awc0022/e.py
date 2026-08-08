n, m = map(int, input().split())
INF = 10**18
d = [[INF] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    d[u][v] = min(d[u][v], w)
    d[v][u] = min(d[v][u], w)

for k in range(n):
    for i in range(n):
        dik = d[i][k]
        if dik == INF:
            continue
        for j in range(n):
            nd = dik + d[k][j]
            if nd < d[i][j]:
                d[i][j] = nd

for i in range(n):
    if d[0][i] == INF:
        print(-1)
        exit()

size = 1 << n
dp = [[INF] * n for _ in range(size)]
dp[1][0] = 0
for mask in range(size):
    if not (mask & 1):
        continue
    for v in range(n):
        if not (mask >> v) & 1:
            continue
        cur = dp[mask][v]
        if cur == INF:
            continue
        for u in range(n):
            if (mask >> u) & 1:
                continue
            nm = mask | (1 << u)
            nv = cur + d[v][u]
            if nv < dp[nm][u]:
                dp[nm][u] = nv

ans = min(dp[size - 1][v] + d[v][0] for v in range(n))
print(ans)
