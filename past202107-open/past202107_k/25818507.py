# Contest ID: past202107-open
# Problem ID: past202107_k ( https://atcoder.jp/contests/past202107-open/tasks/past202107_k )
# Title: K. Flying Trip
# Language: Python (3.8.2)
# Submitted: 2021-09-12 23:39:57 +0000 UTC ( https://atcoder.jp/contests/past202107-open/submissions/25818507 ) 

import heapq

N, M = map(int, input().split())
a = list(map(int, input().split()))
node = [[] for _ in range(N)]

for i in range(M):
    u, v, t = map(int, input().split())
    u -= 1
    v -= 1
    node[u].append((v, t))
    node[v].append((u, t))


inf = 10**17
dist = [inf for _ in range(N)]
cost = [0 for _ in range(N)]

dist[0] = 0
cost[0] = a[0]
pq = [[0,a[0], 0]]
heapq.heapify(pq)


while len(pq) != 0 :
    cur_dist,  cur_val, cur_pos = heapq.heappop(pq)
    if dist[cur_pos] < cur_dist :
        continue
    for e in node[cur_pos]:
        pos = e[0]
        if dist[pos] == dist[cur_pos] + e[1] :
            cost[pos] = max(cost[pos], cost[cur_pos] + a[pos])
        if dist[pos] > dist[cur_pos] + e[1] :
            dist[pos] = dist[cur_pos] + e[1]
            cost[pos] = cost[cur_pos] + a[pos]
            heapq.heappush(pq, [dist[pos], cost[pos], pos])

# print(dist)
# print(cost)
print(cost[N-1])

