N = int(input())
p = list(map(int, input().split()))
w = list(map(int, input().split()))

n = 1 << N
dp = [[0] * N for _ in range(n)]

for bit in range(n) :
    for i in range(N) :
        if (bit>>i)%2 == 0 : continue
        m = bit.bit_count()
        for j in range(N) :
            if (bit>>j)%2 == 1 : continue
            nj = bit | (1<<j)
            imp = abs(p[i] - p[j])*w[m-1]
            dp[nj][j] = max(dp[nj][j], dp[bit][i] + imp)

ans = max(dp[n-1])
print(ans)
