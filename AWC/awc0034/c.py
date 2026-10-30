from atcoder.fenwicktree import FenwickTree

n, k, t, c = map(int, input().split())
a = list(map(int, input().split()))

bit = FenwickTree(n+k+1)

ans = 0
for i in range(n) :
    cur = a[i] + bit.sum(0, i+1)
    rest = max(0, t - cur)
    ans += rest * c
    bit.add(i, rest)
    bit.add(i+k, -rest)

print(ans)