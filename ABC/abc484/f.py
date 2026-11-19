from atcoder.segtree import SegTree

n, q = map(int, input().split())
a = list(map(int, input().split()))

def cmp(a, b) :
    if a == inf or b == inf : return inf
    if a == -1 : return b
    if b == -1 : return a
    if a == b : return a
    return inf

inf = 10**18
seg = SegTree(cmp, -1, a)

for _ in range(q) :
    t, a, b = map(int, input().split())
    if  t == 1:
        i, x = a-1, b
        seg.set(i, x)
    else:
        l, r = a-1, b
        if seg.prod(l, r) == inf :
            print("No")
        else :
            print("Yes")