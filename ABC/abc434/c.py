T = int(input())
for _ in range(T):
    n, h = map(int, input().split())
    lo = hi = h
    pt = 0 
    ok = True
    for __ in range(n):
        t, l, u = map(int, input().split())
        if not ok:
            pt = t
            continue

        dt = t - pt
        lo = max(0, lo-dt)
        hi += dt

        if lo < l:
            lo = l
        if hi > u:
            hi = u

        if lo > hi: 
            ok = False
        pt = t

    print("Yes" if ok else "No")


