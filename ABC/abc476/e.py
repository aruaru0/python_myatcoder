from atcoder.segtree import SegTree

INF = 1 << 60
n, m = map(int, input().split())
p = list(map(int, input().split()))

st = SegTree(lambda a, b: (a[0] if a[0] < b[0] else b[0],
                          a[1] if a[1] > b[1] else b[1]),
             (INF, -1), [(v, v) for v in p])

pos = [0] * (n + 1)
for i, v in enumerate(p):
    pos[v] = i

for _ in range(m):
    l, r = map(int, input().split())
    mn, mx = st.prod(l - 1, r)
    a = pos[mn]
    b = pos[mx]
    p[a], p[b] = p[b], p[a]
    pos[mn], pos[mx] = b, a
    st.set(a, (p[a], p[a]))
    st.set(b, (p[b], p[b]))

print(*p)
