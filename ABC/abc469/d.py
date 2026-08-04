n, m = map(int, input().split())
es = set()
for _ in range(m):
    a, b = map(int, input().split())
    es.add((a, b))
ed = list(es)
u0, v0 = ed[0]


def gval(u):
    su = [(a, b) for a, b in ed if a != u and b != u]
    k = len(su)
    if k == 0:
        return n - 1
    if k == 1:
        return 2
    for p in su[0]:
        if all(a == p or b == p for a, b in su):
            return 1
    return 0


ans = gval(u0) + gval(v0)
if all(a == u0 or b == u0 or a == v0 or b == v0 for a, b in ed):
    ans -= 1
print(ans)
