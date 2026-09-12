from bisect import bisect_left
from atcoder.fenwicktree import FenwickTree

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

# B_i = A_i + M, P_i = sum of first i B's
p = [0] * (n + 1)
for i in range(n):
    p[i + 1] = p[i] + a[i] + m

# coordinate compression of prefix sums
v = sorted(set(p))
idx = {x: i for i, x in enumerate(v)}

fw = FenwickTree(len(v))
fw.add(idx[p[0]], 1)
ans = 0
for j in range(1, n + 1):
    # count i < j with p[i] >= p[j] - k
    t = bisect_left(v, p[j] - k)
    ans += j - fw.sum(0, t)
    fw.add(idx[p[j]], 1)
print(ans)
