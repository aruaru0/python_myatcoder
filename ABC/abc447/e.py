from atcoder import dsu

n, m = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(m) ]

mod = 998244353

cost = [2]
for i in range(m) :
    cost.append(cost[-1] * 2 % mod)

uf = dsu.DSU(n)
ans = 0
g = n
for i in range(m-1, -1, -1) :
    [u, v] = edges[i]
    u-=1
    v-=1
    # print(u, v)
    if uf.same(u, v) :
        continue
    if g > 2 :
        uf.merge(u, v)
        g -= 1
    else :
        ans += cost[i]
        ans %= mod

print(ans)
