n, m = map(int, input().split())

g = [set() for _ in range(n)]

for _ in range(m) :
    a, b = map(int, input().split())
    a-=1
    b-=1
    g[a].add(b)
    g[b].add(a)

ans = []
for i in range(n):
    d = len(g[i])
    r = n - 1 - d
    ans.append(r*(r-1)*(r-2)//6)

print(*ans)