import bisect

n = int(input())
a = list(map(int, input().split()))
a.sort()

k = bisect.bisect_left(a, 0)
if k == 0:
    pl = pr = 0
    ans = a[0]
elif k == n:
    pl = pr = n - 1
    ans = -a[-1]
else:
    dl = -a[k - 1]
    dr = a[k]
    if dl <= dr:
        pl = pr = k - 1
        ans = dl
    else:
        pl = pr = k
        ans = dr
pos = a[pl]

while pl > 0 or pr < n - 1:
    if pl > 0 and (pr == n - 1 or pos - a[pl - 1] <= a[pr + 1] - pos):
        ans += pos - a[pl - 1]
        pos = a[pl - 1]
        pl -= 1
    else:
        ans += a[pr + 1] - pos
        pos = a[pr + 1]
        pr += 1

print(ans)