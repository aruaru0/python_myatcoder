import heapq

n, m = map(int, input().split())

to = [[] for _ in range(n)]
cnt = [0] * n
for i in range(m) :
    a, b = map(int, input().split())
    a-=1
    b-=1
    to[a].append(b)
    cnt[b] += 1

pq = []
for i in range(n) :
    if cnt[i] == 0 :
        heapq.heappush(pq, i)

ans = []
while len(pq) :
    cur = heapq.heappop(pq)
    ans.append(cur+1)
    for e in to[cur] :
        cnt[e]-=1
        if cnt[e] == 0 :
            heapq.heappush(pq, e)

print(*ans)