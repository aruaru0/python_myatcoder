import heapq

N, M = map(int, input().split())
P = list(map(int, input().split()))
S, T = map(int, input().split())
S -= 1
T -= 1

A = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    A[u-1].append((v-1, w))
    A[v-1].append((u-1, w))

INF = -10**18
D = [[INF] * (1 << N) for _ in range(N)]

sm = 1 << S
D[S][sm] = P[S]
Q = [(-P[S], S, sm)]

while Q:
    g, u, m = heapq.heappop(Q)
    g = -g

    if g < D[u][m]:
        continue

    for v, w in A[u]:
        nm = m | (1 << v)
        ng = g - w + (P[v] if nm != m else 0)

        if ng > D[v][nm]:
            D[v][nm] = ng
            heapq.heappush(Q, (-ng, v, nm))

print(max(D[T]))

