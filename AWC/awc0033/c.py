from collections import deque

n, m, k, t = map(int, input().split())
c = list(map(int, input().split()))
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

known = [False] * n
cnt = [0] * n
q = deque()
for x in c:
    x -= 1
    known[x] = True
    q.append(x)

while q:
    u = q.popleft()
    for v in g[u]:
        if not known[v]:
            cnt[v] += 1
            if cnt[v] >= t:
                known[v] = True
                q.append(v)
                
print(sum(known))
