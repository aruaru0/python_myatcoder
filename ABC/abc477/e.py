import sys

INF = 10 ** 30

n, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# c[v]: coordinate of vertex v on the cycle (1-indexed), c[1]=0
c = [0] * (n + 2)
for v in range(2, n + 1):
    c[v] = c[v - 1] + a[v - 2]
tot = c[n] + a[n - 1]

preP = [INF] * (n + 2)  # min (B_i + c[i]) for 1<=i<=v
sufP = [INF] * (n + 2)  # min (B_i + c[i]) for v<=i<=N
preM = [INF] * (n + 2)  # min (B_i - c[i]) for 1<=i<=v
sufM = [INF] * (n + 2)  # min (B_i - c[i]) for v<=i<=N

for v in range(1, n + 1):
    p = b[v - 1] + c[v]
    m = b[v - 1] - c[v]
    preP[v] = preP[v - 1] if preP[v - 1] < p else p
    preM[v] = preM[v - 1] if preM[v - 1] < m else m
for v in range(n, 0, -1):
    p = b[v - 1] + c[v]
    m = b[v - 1] - c[v]
    sufP[v] = sufP[v + 1] if sufP[v + 1] < p else p
    sufM[v] = sufM[v + 1] if sufM[v + 1] < m else m

# D[v]: shortest distance from vertex v to hub (vertex N+1)
d = [0] * (n + 2)
for v in range(1, n + 1):
    cv = c[v]
    x1 = sufP[v] - cv
    x2 = preP[v - 1] + tot - cv
    x3 = preM[v] + cv
    x4 = sufM[v + 1] + tot + cv
    r = x1 if x1 < x2 else x2
    if x3 < r:
        r = x3
    if x4 < r:
        r = x4
    d[v] = r

out = []
for _ in range(q):
    s, t = map(int, input().split())
    if t == n + 1:
        out.append(d[s])
    else:
        x = c[s] - c[t]
        if x < 0:
            x = -x
        y = tot - x
        cd = x if x < y else y
        via = d[s] + d[t]
        out.append(cd if cd < via else via)

sys.stdout.write('\n'.join(map(str, out)) + '\n')
