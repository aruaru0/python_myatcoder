from collections import deque

n, m, k = map(int, input().split())

node = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    if w >= k:
        node[u].append(v)
        node[v].append(u)

inf = 1e18
dist = [-inf] * n

q = deque([0])
dist[0] = 0
while len(q) :
    cur = q.popleft()
    for e in node[cur] :
        if dist[e] == -inf :
            dist[e] = dist[cur] + 1
            q.append(e)

print(dist[n-1] if dist[n-1] != -inf else -1)