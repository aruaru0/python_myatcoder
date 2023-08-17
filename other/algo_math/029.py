n = int(input())

dp = [0 for _ in range(n+2)]

dp[0] = 1

for i in range(n):
    dp[i+1] += dp[i]
    dp[i+2] += dp[i]

print(dp[n])