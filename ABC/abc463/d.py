n, k = map(int, input().split())
lr = [tuple(map(int, input().split())) for _ in range(n)]
lr.sort(key=lambda x: x[1])

def ok(x):
    cnt = 0
    last = -10**18
    for l, r in lr:
        if l >= last + x:
            cnt += 1
            last = r
    return cnt >= k

if not ok(1):
    print(-1)
else:
    lo, hi = 1, 10**9 + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if ok(mid):
            lo = mid
        else:
            hi = mid
    print(lo)
