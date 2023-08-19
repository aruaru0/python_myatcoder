N = int(input())
a = list(map(int, input().split()))

dp = [[0,0] for _ in range(N+1)]
for i in range(N):
    dp[i+1][0] = max(dp[i][0], dp[i][1])
    dp[i+1][1] = dp[i][0] + a[i]


print(max(dp[N]))