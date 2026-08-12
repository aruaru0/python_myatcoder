n, l = map(int, input().split())
a = list(map(int, input().split()))

N = n
prev = [[0.0] * (N + 1) for _ in range(N + 1)]  # L-1層
cur = None
for L in range(1, l + 1):
    cur = [[0.0] * (N + 1) for _ in range(N + 1)]
    for c1 in range(N + 1):
        cur[0][c1] = float(c1)
    g = 1.0 if L >= 2 else 0.0
    for c0 in range(1, N + 1):
        prow = cur[c0 - 1]
        row = cur[c0]
        pm = prev[c0 - 1]
        for c1 in range(0, N - c0 + 1):
            u = 2 * c0 + c1
            p = c1 / u
            w = 1.0 - p
            inv = 1.0 / (u - 1)
            t = p * (1.0 + row[c1 - 1]) if c1 > 0 else 0.0
            t += w * inv * (1.0 + prow[c1])
            if c0 >= 2:
                t += w * (2 * c0 - 2) * inv * prev[c0 - 2][c1 + 2]
            if c1 > 0:
                t += w * c1 * inv * (g + pm[c1])
            row[c1] = t
    prev = cur

x = prev[N][0]
print('%.10f' % (x * sum(a) / n))
