n, m, l, s, t = map(int, input().split())

node = [[] for _ in range(n)]
for _ in range (m) :
    u, v, c = map(int, input().split())
    u-=1
    v-=1
    node[u].append((v, c))


x = set()

def dfs(cur, cnt, cost) :
    if cnt == l :
        if s <= cost <= t :
            x.add(cur+1)
        return
    
    for v, c in node[cur] :
        dfs(v, cnt+1, cost+c)

dfs(0, 0, 0)

ans = sorted(list(x))
print(*ans)