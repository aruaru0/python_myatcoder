# Contest ID: abc185
# Problem ID: abc185_c ( https://atcoder.jp/contests/abc185/tasks/abc185_c )
# Title: C. Duodecim Ferra
# Language: Python (3.8.2)
# Submitted: 2022-03-16 02:29:53 +0000 UTC ( https://atcoder.jp/contests/abc185/submissions/30159558 ) 

L = int(input())

dp = [[0 for _ in range(12)] for _ in range(L+1)]
dp[0][0] = 1
for i in range(1, L) :
    for j in range(0, 12) :
        dp[i][j] += dp[i-1][j]
        if j+1 < 12 :
            dp[i][j+1] += dp[i-1][j]
    # print(dp[i])
print(dp[L-1][11])