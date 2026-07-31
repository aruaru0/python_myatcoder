import sys
from atcoder.segtree import SegTree

n, m = map(int, input().split())

w = list(map(int, input().split()))
c = list(map(int, input().split()))

seg = SegTree(max, -1, c)

cnt = 0
for e in w:
    if seg.all_prod() < e :
        continue

    idx = seg.max_right(0, lambda x: x < e)
    cnt += 1
    seg.set(idx, -1)

print(cnt)
