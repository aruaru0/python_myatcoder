import sys

INF = 10**30

N, Q = map(int, input().split())
L = [INF] + list(map(int, input().split()))
R = list(map(int, input().split())) + [INF]

prefR = [0] * N
cur = INF
for i in range(N):
    if R[i] < cur:
        cur = R[i]
    prefR[i] = cur

suffL = [0] * N
cur = INF
for i in range(N - 1, -1, -1):
    if L[i] < cur:
        cur = L[i]
    suffL[i] = cur

out = []
for _ in range(Q):
    s, t = map(int, input().split())
    si = s - 1
    ti = t - 1
    if si < ti:
        m = prefR[si - 1] if si > 0 else INF
        a = R[si]
        b = L[si] + m
        out.append(a if a < b else b)
    else:
        m = suffL[si + 1] if si < N - 1 else INF
        a = L[si]
        b = R[si] + m
        out.append(a if a < b else b)

sys.stdout.write('\n'.join(map(str, out)) + '\n')
