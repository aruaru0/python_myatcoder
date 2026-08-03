import heapq

n, m, k = map(int,input().split())

node = [[] for _ in range(n)]
for _ in range(m) :
    u, v, t = map(int, input().split())
    u -=1
    v -=1
    node[u].append((v, t))
    node[v].append((u, t))


p = list(map(int, input().split()))
p.append(n)
p = [e-1 for e in p]

inf = 10**18
def dijkstra(start, end) :
    dist = [inf]*n
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while len(pq) != 0 :
        cur_cost, cur = heapq.heappop(pq)
        if dist[cur] < cur_cost :
            continue
        for to, cost in node[cur] :
            if dist[to] > dist[cur] + cost :
                dist[to] = dist[cur] + cost
                heapq.heappush(pq, (dist[to], to))
    return dist[end]

cur, ans = 0,0
for e in p :
    d = dijkstra(cur, e)
    if d == inf :
        print(-1)
        exit()
    ans += d
    cur = e
print(ans)