INF = 1 << 60

n, m = map(int, input().split())
adj = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    if w < adj[u][v]:
        adj[u][v] = w
s, k = map(int, input().split())
tg = list(map(int, input().split()))


def dij(src):
    d = [INF] * (n + 1)
    d[src] = 0
    used = [False] * (n + 1)
    for _ in range(n):
        u = -1
        best = INF
        for v in range(1, n + 1):
            if not used[v] and d[v] < best:
                best = d[v]
                u = v
        if u == -1:
            break
        used[u] = True
        du = d[u]
        row = adj[u]
        for v in range(1, n + 1):
            w = row[v]
            if w < INF and du + w < d[v]:
                d[v] = du + w
    return d


# distance from S, then from each destination
d0 = dij(s)
dd = [dij(t) for t in tg]

full = (1 << k) - 1
dp = [[INF] * k for _ in range(1 << k)]
for i in range(k):
    dp[1 << i][i] = d0[tg[i]]

for mask in range(1 << k):
    row = dp[mask]
    for i in range(k):
        cur = row[i]
        if cur >= INF:
            continue
        di = dd[i]
        for j in range(k):
            if mask >> j & 1:
                continue
            nd = cur + di[tg[j]]
            if nd < dp[mask | 1 << j][j]:
                dp[mask | 1 << j][j] = nd

ans = INF
for i in range(k):
    v = dp[full][i]
    if v >= INF:
        continue
    e = dd[i][s]
    if v + e < ans:
        ans = v + e
print(-1 if ans >= INF else ans)
