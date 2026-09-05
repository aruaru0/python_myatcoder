from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))


def cnt(x):
    # count intervals with max-min <= x, two pointers + monotonic deques
    if x < 0:
        return 0
    qmx = deque()  # indices, A decreasing (front = max)
    qmn = deque()  # indices, A increasing (front = min)
    r = 0
    res = 0
    for l in range(n):
        while r < n:
            mx = a[r] if not qmx else max(a[qmx[0]], a[r])
            mn = a[r] if not qmn else min(a[qmn[0]], a[r])
            if mx - mn > x:
                break
            while qmx and a[qmx[-1]] <= a[r]:
                qmx.pop()
            qmx.append(r)
            while qmn and a[qmn[-1]] >= a[r]:
                qmn.pop()
            qmn.append(r)
            r += 1
        res += r - l
        if qmx and qmx[0] == l:
            qmx.popleft()
        if qmn and qmn[0] == l:
            qmn.popleft()
    return res


print(cnt(k) - cnt(k - 1))