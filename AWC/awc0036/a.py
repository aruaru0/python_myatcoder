N = int(input())
p = []
for _ in range(N) :
    l = list(map(int, input().split()))
    p.append(l[1:])

Q = int(input())

cnt = 0
for _ in range(Q) :
    u, d = map(int, input().split())
    u-=1
    d-=1
    if p[u][d] == 0 :
       cnt += 1
    else:
        p[u][d] -= 1


for e in p :
    print(*e)
print(cnt) 