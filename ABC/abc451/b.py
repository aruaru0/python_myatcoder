n,m = map(int, input().split())

cur = [0] * m
nxt = [0] * m

for i in range(n):
    a, b = map(int, input().split())
    cur[a-1] += 1
    nxt[b-1] += 1


c  = [cur[i]-nxt[i] for i in range(m)]

print(*c, sep="\n")