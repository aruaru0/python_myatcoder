N, A, B = map(int, input().split())

dp = [[[0 for _ in range(B+1)] for _ in range(A+1)] for _ in range(N+1)]


for n in range(N):
    w, v = map(int, input().split())
    for i in range(A+1) :
        for j in range(B+1) :
            dp[n+1][i][j] = dp[n][i][j]
            if i-w >= 0 :
                dp[n+1][i][j] = max(dp[n+1][i][j], dp[n][i-w][j]+v)
            if j-w >= 0 :
                dp[n+1][i][j] = max(dp[n+1][i][j], dp[n][i][j-w]+v)
    
print(dp[N][A][B])