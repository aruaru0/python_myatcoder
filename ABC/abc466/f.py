import sys
import heapq

def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    b = []
    for v in a:
        if not b or v < b[-1]:
            b.append(v)

    pq = [(-(x + 1), 1)]

    for v in b:
        while pq and -pq[0][0] > v:
            neg_val, cnt = heapq.heappop(pq)
            val = -neg_val
            while pq and -pq[0][0] == val:
                cnt += heapq.heappop(pq)[1]
            q = val // v
            r = val % v
            heapq.heappush(pq, (-v, q * cnt))
            if r:
                heapq.heappush(pq, (-r, cnt))

    ans = -1
    while pq:
        ans += heapq.heappop(pq)[1]
    print(ans)

t = int(input())
for _ in range(t):
    solve()
