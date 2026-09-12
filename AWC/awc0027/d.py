import heapq

n, m = map(int, input().split())
ds = []
for _ in range(n):
    h, s = map(int, input().split())
    ds.append((h, s))
ps = sorted(map(int, input().split()))

ds.sort()
pq = []
tot = 0
idx = 0
ok = True
for p in ps:
    while idx < n and ds[idx][0] <= p:
        heapq.heappush(pq, -ds[idx][1])
        idx += 1
    if not pq:
        ok = False
        break
    tot += -heapq.heappop(pq)
print(tot if ok else -1)