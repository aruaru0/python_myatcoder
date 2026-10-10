from atcoder.maxflow import MFGraph

n, k, m = map(int, input().split())
b = list(map(int, input().split()))
w = list(map(int, input().split()))
us = []
vs = []
cs = []
for _ in range(m):
    u, v, c = map(int, input().split())
    us.append(u - 1)
    vs.append(v - 1)
    cs.append(c)
q = int(input())
ss = [int(input()) for _ in range(q)]

tot = sum(b)
src = n + k
snk = n + k + 1
alive = [True] * k
for t in range(q):
    alive[ss[t] - 1] = False
    g = MFGraph(n + k + 2)
    for j in range(k):
        if alive[j]:
            g.add_edge(src, n + j, w[j])
    for i in range(n):
        g.add_edge(i, snk, b[i])
    for j in range(m):
        g.add_edge(us[j], vs[j], cs[j])
        g.add_edge(vs[j], us[j], cs[j])
    print("Yes" if g.flow(src, snk) == tot else "No")
