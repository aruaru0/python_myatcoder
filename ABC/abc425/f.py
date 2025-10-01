MOD = 998244353

N = int(input())
T = input()

n = 1 << N


dp = [0] * n
dp[n-1] = 1

for bit in range(n-1, -1, -1) :
    pre = None
    for i in range(N) :
        if (bit>>i)%2 :
            if pre != T[i] :
                dp[bit^(1<<i)] += dp[bit]
                dp[bit^(1<<i)] %= MOD

            pre = T[i]

print(dp[0])