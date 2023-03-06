# Contest ID: abc185
# Problem ID: abc185_c ( https://atcoder.jp/contests/abc185/tasks/abc185_c )
# Title: C. Duodecim Ferra
# Language: Python (3.8.2)
# Submitted: 2022-03-15 23:38:34 +0000 UTC ( https://atcoder.jp/contests/abc185/submissions/30157873 ) 

N = 201
C = [[0 for _ in range(N)] for _ in range(N)]

C[0][0] = 1
for i in range(1, N) :
    for j in range (0, N) : 
        if j == 0 or j == i :
            C[i][j] = 1
        else :
            C[i][j] = C[i-1][j-1] + C[i-1][j]



L = int(input())
print(C[L-1][11])