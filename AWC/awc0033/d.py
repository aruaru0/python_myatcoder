import heapq

n, m, k = map(int, input().split())

class Edge :
    to : int
    cost : int
    def __init__(self, to, cost):
        self.to = to
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

node = [[] for _ in range(n)]
for i in range(m):
    u, v, c = map(int, input().split())
    u-=1
    v-=1
    node[u].append(Edge(v, c))
    node[v].append(Edge(u, c))

INF = 10**18
dist = [INF] * n
pq = []
    # (cost, to)
heapq.heappush(pq, (0, 0))

while pq:
    cur_cost, cur_to = heapq.heappop(pq)
    
    if cur_cost > dist[cur_to]:
        continue
        
    for e in node[cur_to]:
        if dist[e.to] > cur_cost + e.cost: 
            dist[e.to] = cur_cost + e.cost
            heapq.heappush(pq, (dist[e.to], e.to))

ans = dist[n-1]
if ans > k :
    print(-1)
else:
    print(ans)