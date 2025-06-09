import atcoder.fenwicktree as ft

N, Q = map(int, input().split())

bit = ft.FenwickTree(N)
for i, v in enumerate(list(map(int, input().split()))):
    bit.add(i, v)


for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 0 :
        bit.add(x, y)
    else :
        print(bit.sum(x, y))