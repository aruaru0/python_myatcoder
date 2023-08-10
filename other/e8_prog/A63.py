from collections import deque

N, M = map(int, input().split())

node = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node[a].append(b)
    node[b].append(a)


inf = 10**9
dist = [inf for _ in range(N)]

dist[0] = 0
q = deque([0])

while len(q) != 0 :
    cur = q[0]
    q.popleft()
    for e in node[cur]:
        if dist[e] > dist[cur] + 1 :
            dist[e] = dist[cur]+1
            q.append(e)


for e in dist:
    if e == inf : print(-1)
    else:
        print(e)

