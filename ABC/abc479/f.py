from atcoder.fenwicktree import FenwickTree

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

p = sorted(range(N), key=lambda i: S[i])
Sx = [S[i] for i in p]
Tx = [T[i] for i in p]

ts = sorted(T)
rk = {v: i + 1 for i, v in enumerate(ts)}
rn = [rk[v] for v in Tx]

p1 = 0
for x in range(1, N + 1):
    p1 += abs((Sx[x - 1] - x) - (Tx[x - 1] - rn[x - 1]))

q = sorted(range(N), key=lambda i: Tx[i])
sq = [Sx[i] for i in q]

vals = sorted(sq)
ix = {v: i for i, v in enumerate(vals)}
bit = FenwickTree(N)
inv = 0
for i, v in enumerate(sq):
    r = ix[v]
    le = bit.sum(0, r + 1)
    inv += i - le
    bit.add(r, 1)

print(p1 + inv)
