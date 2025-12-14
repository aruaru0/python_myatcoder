n = int(input())

a = [[0 for _ in range(n)] for _ in range(n)]

r, c = 0, (n-1)//2
cur = 1
a[r][c] = cur
for _ in range(n*n-1):
    cur += 1
    nr, nc = (r-1)%n, (c+1)%n
    if a[nr][nc] != 0 :
        nr, nc = (r+1)%n, c
    a[nr][nc] = cur
    r, c = nr, nc


for i in range(n):
    print(*a[i])