N, Q = map(int, input().split())
v = list(map(int, input().split()))

for _ in range(Q):
    t = list(map(int, input().split()))
    if t[0] == 1 :
        a, b = t[1]-1, t[2]-1
        v[b] += v[a]
        v[a] = 0
    else:
        c = t[1]-1
        print(v[c])

    