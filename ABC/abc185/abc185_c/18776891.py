# Contest ID: abc185
# Problem ID: abc185_c ( https://atcoder.jp/contests/abc185/tasks/abc185_c )
# Title: C. Duodecim Ferra
# Language: Python (3.8.2)
# Submitted: 2020-12-14 06:27:08 +0000 UTC ( https://atcoder.jp/contests/abc185/submissions/18776891 ) 

l = int(input())

dp = [[0 for _ in range(l+1)] for _ in range(13)]

dp[0][0] = 1
for i in range(1, 13):
    for j in range(1, l + 1):
        tot = 0
        for k in range(0, j):
            tot += dp[i - 1][k]
        dp[i][j] = tot

print(dp[12][l])
