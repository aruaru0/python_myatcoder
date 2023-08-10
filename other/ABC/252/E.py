import heapq

N, M = map(int, input().split())

node = [[] for _ in range(N)]
for i in range(M) :
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    node[a].append((b, c, i))
    node[b].append((a, c, i))


inf = int(1e18)
dist = [inf for _ in range(N)]
dist[0] = 0
pq = []
heapq.heappush(pq, (0, 0, -1))

used = [False for _ in range(M)]

while len(pq) != 0 :
    cur_cost, cur, idx = pq[0]
    heapq.heappop(pq)
    if cur_cost > dist[cur] : continue
    if idx >= 0 :
        used[idx] = True
    for e, cost, i in node[cur]:
        if dist[e] > dist[cur] + cost :
            dist[e] = dist[cur] + cost
            heapq.heappush(pq, (dist[e], e, i))


# print(used)
ans = []
for i in range(M):
    if used[i] : ans.append(i+1)

print(*ans)