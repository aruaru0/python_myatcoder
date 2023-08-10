import heapq

N, M = map(int, input().split())

node = [[] for _ in range(N)]
for i in range(M) :
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    node[a].append((b, c))
    node[b].append((a, c))


inf = int(1e18)
dist = [inf for _ in range(N)]
dist[0] = 0
pq = []
heapq.heappush(pq, (0, 0))


while len(pq) != 0 :
    cur_cost, cur  = pq[0]
    heapq.heappop(pq)
    if cur_cost > dist[cur] : continue
    for e, cost in node[cur]:
        if dist[e] > dist[cur] + cost :
            dist[e] = dist[cur] + cost
            heapq.heappush(pq, (dist[e], e))

for e in dist:
    if e == inf : print(-1)
    else : print(e)
