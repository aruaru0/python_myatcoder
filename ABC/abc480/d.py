n, q = map(int, input().split())
a = list(map(int, input().split()))

# pa[i] = A_1+...+A_i, pm[i] = 1*A_1+...+i*A_i  (0-indexed prefix arrays)
pa = [0] * (n + 1)
pm = [0] * (n + 1)
for i in range(n):
    pa[i + 1] = pa[i] + a[i]
    pm[i + 1] = pm[i] + (i + 1) * a[i]


def F(t):
    # sum of B_1..B_t
    if t <= 0:
        return 0
    # smallest i with i*(i+1)/2 >= t
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) // 2
        if mid * (mid + 1) // 2 >= t:
            hi = mid
        else:
            lo = mid + 1
    i = lo
    k = t - (i - 1) * i // 2  # offset inside block i (1..i)
    return i * pa[i - 1] - pm[i - 1] + pa[k]


out = []
for _ in range(q):
    l, r = map(int, input().split())
    out.append(F(r) - F(l - 1))
print("\n".join(map(str, out)))
