import heapq


X = int(input())
Q = int(input())
L = [-X]
R = []
for _ in range(Q):
    A, B = map(int, input().split())
    for v in (A, B):
        if v <= -L[0]:
            heapq.heappush(L, -v)
        else:
            heapq.heappush(R, v)
        if len(L) < len(R):
            heapq.heappush(L, -heapq.heappop(R))
        elif len(L) > len(R) + 1:
            heapq.heappush(R, -heapq.heappop(L))
    print(-L[0])

