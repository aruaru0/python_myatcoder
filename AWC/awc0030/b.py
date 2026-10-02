n, m = map(int, input().split())

vegetable = {}
meet = {}
for i in range(n) :
    p, t = map(int, input().split())
    if t == 0 :
        vegetable[i] = p
    else :
        meet[i] = p

inf = 10**10

for _ in range(m) :
    k = list(map(int, input().split()))

    ve, me = inf, inf
    for e in k[1:] :
        e -= 1
        if e in vegetable :
            ve = min(ve, vegetable[e])
        if e in meet :
            me = min(me, meet[e])

    if ve == inf or me == inf :
        print(-1)
    else:
        print(ve+me)

