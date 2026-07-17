N, M, T = map(int, input().split())
fv = 0
items = []
for _ in range(N):
    a, b, c = map(int, input().split())
    if b >= T:
        fv += a
    else:
        items.append((c, a))

dp = [0] * (M + 1)
for c, a in items:
    for w in range(M, c - 1, -1):
        if dp[w - c] + a > dp[w]:
            dp[w] = dp[w - c] + a

print(fv + dp[M])
