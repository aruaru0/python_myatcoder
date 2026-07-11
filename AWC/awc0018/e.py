n, k, b = map(int, input().split())

INF = 10 ** 18
dp = [[INF] * (b + 1) for _ in range(k + 1)]
dp[0][0] = -1

for _ in range(n):
    c, s = map(int, input().split())
    for j in range(k - 1, -1, -1):
        for x in range(b - c, -1, -1):
            if dp[j][x] < s:
                if s < dp[j + 1][x + c]:
                    dp[j + 1][x + c] = s

ans = 0
for j in range(k + 1):
    for x in range(b + 1):
        if dp[j][x] < INF:
            ans = max(ans, j)

print(ans)
