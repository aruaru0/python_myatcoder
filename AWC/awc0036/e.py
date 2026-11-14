n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
if n > m:
    a = [list(r) for r in zip(*a)]
    n, m = m, n

acc = [0] * (1 << n)
for j in range(m):
    col = [a[i][j] for i in range(n)]
    c = sum(col)
    ss = [0]
    for x in col:
        ss += [v + x for v in ss]
    acc = [u + (v if v > c else c) for u, v in zip(acc, ss)]

print(max(acc))
