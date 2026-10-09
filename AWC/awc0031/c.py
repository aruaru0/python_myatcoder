n, d, s, t = map(int,input().split())
s -= 1
t -= 1

x = [0]*n
y = [0]*n
for i in range(n):
    x[i], y[i] = map(int,input().split())

node = [[] for _ in range(n)]
for i in range(n) :
    for j in range(i+1, n):
        dx, dy = x[i] - x[j], y[i] - y[j]
        dist = dx*dx + dy*dy
        if dist <= d*d :
            node[i].append(j)
            node[j].append(i)

inf = 1e18
q = [s]
dist = [inf]*n
dist[s] = 0
while q :
    v = q.pop(0)
    for nv in node[v] :
        if dist[nv] == inf :
            dist[nv] = dist[v] + 1
            q.append(nv)

print(dist[t] if dist[t] != inf  else -1)
