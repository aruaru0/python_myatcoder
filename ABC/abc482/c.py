import bisect

h, w, n, q = map(int, input().split())

r = [0]*n
c = [0]*n
for i in range(n) :
    r[i], c[i] = map(int, input().split())

r.sort()
c.sort()

def cnt(l, r, v) :
    return bisect.bisect_right(v, r) - bisect.bisect_left(v, l)

for _ in range(q) :
    t, x, y = map(int, input().split())
    if t == 1 :
        print(cnt(x, y, r))
    else:
        print(cnt(x, y, c))

