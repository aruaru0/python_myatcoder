from atcoder.scc import SCCGraph

n, q = map(int, input().split())
g = SCCGraph(n)
ts = [0] * q
us = [0] * q
vs = [0] * q
for i in range(q):
    t, u, v = map(int, input().split())
    u -= 1
    v -= 1
    ts[i] = t
    us[i] = u
    vs[i] = v
    g.add_edge(u, v)

ids = [0] * n
for c, grp in enumerate(g.scc()):  # トポロジカル順
    for x in grp:
        ids[x] = c

# 強連結成分内に strict な辺があると矛盾
for i in range(q):
    if ts[i] == 1 and ids[us[i]] == ids[vs[i]]:
        print("No")
        break
else:
    print("Yes")
    print(*[ids[i] + 1 for i in range(n)])
