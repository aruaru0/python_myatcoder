from collections import deque

n, m, s, t = map(int, input().split())
s-=1
t-=1

node = [[] for _ in range(n)]
for _ in range(m) :
    u, v = map(int, input().split())
    u-=1
    v-=1
    node[u].append(v)

for i in range(n):
    node[i].sort()

INF = 1e9
dist = [INF] * n
q = deque()

q.append(s)
dist[s] = 0

while len(q) != 0 :
    cur = q.popleft()

    for i, next in enumerate(node[cur]) :
        cost = 0 if i == 0 else 1
        if dist[next] > dist[cur] + cost :
            dist[next] = dist[cur] + cost 
            if cost == 0 :
                q.appendleft(next)
            else :
                q.append(next)


ans = dist[t]
if ans == INF :
    print(-1)
else :
    print(ans)