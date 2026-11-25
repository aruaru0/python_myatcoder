from collections import deque

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, c = map(int, input().split())
    g[u].append((v, c))

c1 = [-1] * (n + 1)
c2 = [-1] * (n + 1)
q = deque([(1, 0, 0)])
ans = -1
while q:
    v, col, d = q.popleft()
    if v == n:
        ans = d
        break
    if c1[v] == -1:
        c1[v] = col
        for w, cc in g[v]:
            if cc != col:
                q.append((w, cc, d + 1))
    elif c2[v] == -1 and col != c1[v]:
        c2[v] = col
        f = c1[v]
        for w, cc in g[v]:
            if cc == f:
                q.append((w, cc, d + 1))
print(ans)
