from atcoder.fenwicktree import FenwickTree
B = 500

n, q = map(int, input().split())
seg = FenwickTree(n+1)
S = list(map(int,input().split()))

for i, s in enumerate(S, 1):
    seg.add(i, s)

memo = [0] * B
for _ in range(q):
    t, *other = map(int, input().split())
    if t == 1:
        k, v = other
        if k < B:
            memo[k] += v
        else:
            for i in range(k, n + 1, k):
                seg.add(i, v)
    else:
        x, = other
        ans = seg.sum(0, x+1)
        for i in range(1, B):
            ans += (x // i) * memo[i]
        print(ans)
