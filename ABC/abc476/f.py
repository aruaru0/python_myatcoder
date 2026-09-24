n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ln = 2 * n - 1
of = n - 1
wa = [0] * ln
va = [0] * ln

for i in range(n):
    ai = a[i]
    bw = i
    bv = i + of
    for j in range(n):
        p = (ai * b[j]) % m
        wa[bw + j] += p
        va[bv - j] += p


def trs(c):
    l = len(c)
    pw = [0] * (l + 1)
    px = [0] * (l + 1)
    for k in range(l):
        pw[k + 1] = pw[k] + c[k]
        px[k + 1] = px[k] + c[k] * k
    totw = pw[l]
    totx = px[l]
    res = [0] * l
    for d in range(l):
        le = d * pw[d + 1] - px[d + 1]
        ri = (totx - px[d + 1]) - d * (totw - pw[d + 1])
        res[d] = le + ri
    return res


t1 = trs(wa)
t2 = trs(va)

ans = 0
for i in range(n):
    d1 = i
    d2 = i + of
    base = i * n
    for j in range(n):
        f = (t1[d1 + j] + t2[d2 - j]) >> 1
        ans ^= f + base + j
print(ans)
