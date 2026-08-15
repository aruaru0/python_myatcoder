n, c = map(int, input().split())
w = list(map(int, input().split()))

INF = 10 ** 18
S = 1 << n
dp = [INF] * S
rm = [0] * S
dp[0] = 1
rm[0] = c

for m in range(S):
    if dp[m] >= INF:
        continue
    for i in range(n):
        if m >> i & 1: # すでに含まれていたらスキップ
            continue
        nm = m | (1 << i) # next m
        if rm[m] >= w[i]: # 残り容量に入るなら
            t = dp[m]
            r = rm[m] - w[i]
        else: # 入らないなら
            t = dp[m] + 1
            r = c - w[i]
        if t < dp[nm] or (t == dp[nm] and r > rm[nm]):
            dp[nm] = t
            rm[nm] = r

print(dp[S - 1])
