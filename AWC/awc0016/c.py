import heapq
N, L, R, T = map(int, input().split())

q = []
for i in range(N):
    p, s = map(int, input().split())
    if L <= p <= R and T <= s:
        heapq.heappush(q, (p, -s, i+1))


if len(q) == 0 :
    print(-1)
else:
    print(q[0][2])

    