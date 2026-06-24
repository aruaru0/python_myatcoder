import heapq

N, M, Y = map(int, input().split())

g = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, t = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append((v, t))
    g[v].append((u, t))

X = list(map(int, input().split()))

vn = N
for i in range(N):
    g[i].append((vn, X[i]))
    g[vn].append((i, X[i] + Y))

INF = 10 ** 30
dist = [INF] * (N + 1)
dist[0] = 0
q = [(0, 0)]

while q:
    d, v = heapq.heappop(q)
    if d > dist[v]:
        continue
    for to, w in g[v]:
        nd = d + w
        if nd < dist[to]:
            dist[to] = nd
            heapq.heappush(q, (nd, to))

print(" ".join(str(dist[i]) for i in range(1, N)))
