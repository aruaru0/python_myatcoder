import collections
import sys

N, M = [int(x) for x in input().split()]
if N == 1:
    for m in range(M):
        print(1 if m == 1 % M else -1)
    sys.exit(0)

f = []
for i in range(2, 10**8):
    if i * i > N:
        break
    c = 0
    while N % i == 0:
        N //= i
        c += 1
    if c > 0:
        f.append((i % M, c))
if N != 1:
    f.append((N % M, 1))
    N = 1

inf = 10**18
d = [[inf] * M for i in range(len(f))]
Q = collections.deque()

d[0][1 % M] = 0
Q.appendleft((0, 1 % M, 0))
while len(Q):
    i, j, dij = Q.popleft()
    if d[i][j] != dij:
        continue
    ni = (i + 1) % len(f)
    nd = dij + (1 if i == 0 else 0)
    nj = j
    for e in range(f[i][1] + 1):
        if nd < d[ni][nj]:
            d[ni][nj] = nd
            if i == 0:
                Q.append((ni, nj, nd))
            else:
                Q.appendleft((ni, nj, nd))
        nj = nj * f[i][0] % M

ans = [inf] * M
for i in range(len(f)):
    for j in range(M):
        ans[j] = min(ans[j], max(1, d[i][j]))
for j in range(M):
    if ans[j] == inf:
        ans[j] = -1
print("\n".join(map(str, ans)))
