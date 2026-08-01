n,m = map(int, input().split())
p = list(map(int, input().split()))

for _ in range(n) :
    x = list(map(int, input().split()))

    c = []
    for e in x[1:] :
        c.append((e, p[e-1]))

    c.sort(key = lambda x: (-x[1], x[0]))
    if len(c) == 0 :
        print(0)
    else :
        print(c[0][0])