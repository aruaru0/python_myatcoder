from atcoder.segtree import SegTree

n, k = map(int, input().split())
a = list(map(int, input().split()))

INF = 10**18
seg = SegTree(min, INF, [0]*n)

seg.set(0, a[0])
for r in range(1, n) :
    l = max(0, r-k)
    seg.set(r, seg.prod(l, r)+a[r])

print(seg.get(n-1))