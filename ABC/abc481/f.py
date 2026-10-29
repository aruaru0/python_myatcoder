import sys
from collections import deque

MOD = 998244353

input = sys.stdin.buffer.readline
n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a - 1].append((b - 1, c))

val = [-1] * n
val[0] = 0
dq = deque()
dq.append(([0], 0))
while dq:
    vs, p = dq.popleft()
    for d in range(1, 10):
        nd = (p * 10 + d) % MOD
        nl = []
        for v in vs:
            for b, c in adj[v]:
                if c == d and val[b] < 0:
                    val[b] = nd
                    nl.append(b)
        if nl:
            dq.append((nl, nd))

sys.stdout.write('\n'.join(str(val[v]) for v in range(1, n)) + '\n')
