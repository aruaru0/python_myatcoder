n = int(input())

cost = [[0]*n for _ in range(n)]
for i in range(n-1) :
    cost[i] = [0]*(i+1) + list(map(int, input().split()))


for a in range(n):
    for b in range(a+1, n):
        for c in range(b+1, n) :
            if cost[a][c] > cost[a][b] + cost[b][c] :
                print("Yes")
                exit()

print("No")

