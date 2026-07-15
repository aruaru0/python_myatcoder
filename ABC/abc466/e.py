N, K = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b

INF_NEG = -10**18

dp = [INF_NEG] * (K + 1)
active = [INF_NEG] * (K + 1)
dp[0] = 0

for i in range(N):
    d = B[i] - A[i]
    nd = [INF_NEG] * (K + 1)
    na = [INF_NEG] * (K + 1)
    for j in range(K + 1):
        # not in a segment -> can stay not in segment
        nd[j] = dp[j]
        # was in a segment -> can end the segment (go to not in segment)
        if active[j] > nd[j]:
            nd[j] = active[j]
    for j in range(1, K + 1):
        # start a new segment at i
        cand = dp[j - 1] + d
        if cand > na[j]:
            na[j] = cand
        # continue an existing segment
        cand = active[j] + d
        if cand > na[j]:
            na[j] = cand
    dp = nd
    active = na

best = 0
for j in range(K + 1):
    if dp[j] > best:
        best = dp[j]
    if active[j] > best:
        best = active[j]

print(sum(A) + best)
