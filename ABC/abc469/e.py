n, k = map(int, input().split())
s = input().strip()
m = s.count('o')
st = [0.0] * (m + 1)


def chk(r):
    one = 1.0 - r
    neg = -r
    mn = float('inf')
    pr = 0.0
    j = 0
    for c in s:
        if c == 'o':
            j += 1
            st[j] = pr
            pr += one
            if j >= k:
                v = st[j - k + 1]
                if v < mn:
                    mn = v
                if pr - mn >= 0.0:
                    return True
        else:
            pr += neg
    return False


lo = 0.0
hi = 1.0
for _ in range(25):
    mid = (lo + hi) / 2
    if chk(mid):
        lo = mid
    else:
        hi = mid
print(lo)
