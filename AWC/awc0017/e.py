INF = 10**18

n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    xi, yi = map(int, input().split())
    x[i] = xi
    y[i] = yi

dist = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        dx = x[i] - x[j]
        dy = y[i] - y[j]
        dist[i][j] = dx * dx + dy * dy

size = 1 << n
dp = [[INF] * n for _ in range(size)]
dp[1][0] = 0

for mask in range(1, size):
    for v in range(n):
        if dp[mask][v] == INF:
            continue
        if not (mask >> v & 1):
            continue
        for u in range(n):
            if mask >> u & 1:
                continue
            nmask = mask | (1 << u)
            nd = dp[mask][v] + dist[v][u]
            if nd < dp[nmask][u]:
                dp[nmask][u] = nd

ans = min(dp[size - 1][v] + dist[v][0] for v in range(n))
print(ans)
