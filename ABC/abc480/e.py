from math import isqrt

N = int(input())
n8 = 8 * N
ans = 0

# 長さ3: a(a+d)(a+2d) <= N を満たす d の個数
a = 1
while a * (a + 1) * (a + 2) <= N:
    q = a * a
    d = (isqrt(q * q + n8 * a) - 3 * q) // (4 * a)
    while a * (a + d + 1) * (a + 2 * d + 2) <= N:
        d += 1
    ans += d
    a += 1

# 長さ4以上: a を増やすと最大公差は単調に減る
L = 4
f = 6
while f * L <= N:
    f *= L
    a = 1
    lo = hi = 1
    while True:
        p = 1
        x = a
        for _ in range(L):
            p *= x
            if p > N:
                break
            x += hi
        if p > N:
            break
        lo = hi
        hi *= 2
    while lo < hi:
        m = (lo + hi + 1) // 2
        p = 1
        x = a
        for _ in range(L):
            p *= x
            if p > N:
                break
            x += m
        if p > N:
            hi = m - 1
        else:
            lo = m
    d = lo
    while True:
        ans += d
        a += 1
        p = 1
        x = a
        for _ in range(L):
            p *= x
            if p > N:
                break
            x += 1
        if p > N:
            break
        while True:
            p = 1
            x = a
            for _ in range(L):
                p *= x
                if p > N:
                    break
                x += d
            if p <= N:
                break
            d -= 1
    L += 1

print(ans)
