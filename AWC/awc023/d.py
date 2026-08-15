n, s, t = map(int, input().split())
it = []
for _ in range(n):
    p, c, w = map(int, input().split())
    v = p - c
    if v > 0 and w <= s:
        it.append((v, w))

if sum(v for v, _ in it) < t:
    print(-1)
    raise SystemExit

NEG = -10**18
dp = [[NEG] * (s + 1) for _ in range(len(it) + 1)]
dp[0][0] = 0
mx = 0
for v, w in it:
    lim = s - w
    for k in range(mx, -1, -1):
        dk = dp[k]
        dk1 = dp[k + 1]
        for wt in range(lim, -1, -1):
            x = dk[wt]
            if x != NEG:
                y = x + v
                if y > dk1[wt + w]:
                    dk1[wt + w] = y
    mx += 1

ans = -1
for k in range(1, len(it) + 1):
    if max(dp[k]) >= t:
        ans = k
        break
print(ans)
