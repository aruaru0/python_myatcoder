N = int(input())

C = [[0 for _ in range(N)] for _ in range(2)]

for i in range(N):
    c, p = map(int, input().split())
    C[c-1][i] = p

tot = [[0 for _ in range(N+1)] for _ in range(2)]

for i in range(2) :
    for j in range(N) :
        tot[i][j+1] = tot[i][j] + C[i][j]     


Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    # print("lr", l, r)
    x1 = tot[0][r] - tot[0][l-1]
    x2 = tot[1][r] - tot[1][l-1]
    print(x1, x2)

# print(C) 
# print(tot)