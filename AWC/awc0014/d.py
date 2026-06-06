
import heapq 

N, M, T = map(int, input().split())

node = [[] for _ in range(N)]
for _ in range(M) :
    a, b, c = map(int, input().split())
    a-=1
    b-=1
    node[a].append((b, c))
    node[b].append((a, c))

inf = 10**18
dist = [inf] * N
dist[0] = 0
pq = []
heapq.heappush(pq, (0,0))

while len(pq) != 0 :
    cost, u = pq[0]
    heapq.heappop(pq)
    if dist[u] < cost :
        continue
    for v, c in node[u] :
        if dist[v] > dist[u] + c :
            dist[v] = dist[u] + c
            heapq.heappush(pq, (dist[v], v))

if dist[T-1] == inf :
    print(-1)
else:
    print(dist[T-1]*2)

