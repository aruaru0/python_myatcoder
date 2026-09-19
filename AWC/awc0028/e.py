n, k = map(int, input().split())
a = list(map(int, input().split()))
p = list(map(int, input().split()))

mod = 10**9 + 7
dp = [0] * (k+1)

dp[0] = 1
for i in range(n) :
    for j in range(k-1, -1, -1) :
        if a[i] == p[j] :
            dp[j+1] += dp[j]
            dp[j+1] %= mod

print(dp[k])