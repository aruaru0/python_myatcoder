import heapq

N, M = map(int, (input().split()))


node = [[] for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    node[a].append((b,c))
    node[b].append((a,c))

inf = 10**18

def dijkstra(start) :
    dist = [inf for _ in range(N)]
    dist[start] = 0
    pq = [(0,start)]
    while len(pq) != 0 :
        cur_cost, cur = pq[0]
        heapq.heappop(pq)
        if dist[cur] < cur_cost : continue

        for to, cost in node[cur] :
            if dist[to] > dist[cur] + cost :
                dist[to] = dist[cur] + cost
                heapq.heappush(pq, (dist[to], to))
    return dist

d0 = dijkstra(0)

# print(d0)

if d0[-1] == inf :
    print(-1)
else :
    print(d0[-1])

