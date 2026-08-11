N, Q = map(int, input().split())
p = [e-1 for e in map(int, input().split())]
q = [0]*N
for i in range(N) :
    q[p[i]] = i

for _ in range(Q) :
    t = list(map(int, input().split()))
    if t[0] == 1 :
        x, y = t[1]-1, t[2]-1
        a, b = p[x], p[y]
        p[x], p[y] = p[y], p[x]
        q[a], q[b] = q[b], q[a]
    else :
        p, q = q, p

print(*[e+1 for e in p])


