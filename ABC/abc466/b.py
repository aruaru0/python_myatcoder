n,m= map(int, input().split())

cs = [list(map(int, input().split())) for _ in range(n)]

mx = [-1]*m
for c, s in cs :
    c -= 1
    mx[c] = max(mx[c], s)

print(*mx)
    