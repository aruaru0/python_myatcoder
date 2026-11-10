n = int(input())
a = list(map(int, input().split()))

p = [0] * (n + 1)
for k in range(n):
    p[k + 1] = p[k] + a[k]

pmn = [0] * (n + 1)
pmx = [0] * (n + 1)
pmn[0] = pmx[0] = 0
for k in range(1, n + 1):
    pmn[k] = pmn[k - 1] if pmn[k - 1] < p[k] else p[k]
    pmx[k] = pmx[k - 1] if pmx[k - 1] > p[k] else p[k]

INF = 10 ** 30
smn = [INF] * (n + 2)
smx = [-INF] * (n + 2)
for k in range(n, -1, -1):
    smn[k] = p[k] if p[k] < smn[k + 1] else smn[k + 1]
    smx[k] = p[k] if p[k] > smx[k + 1] else smx[k + 1]

ans = pmx[n] - pmn[n] + 1

for i in range(1, n + 1):
    d = 2 * a[i - 1]
    lo = pmn[i - 1]
    t = smn[i] - d
    if t < lo:
        lo = t
    hi = pmx[i - 1]
    t = smx[i] - d
    if t > hi:
        hi = t
    v = hi - lo + 1
    if v > ans:
        ans = v

print(ans)
