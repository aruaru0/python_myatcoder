
n = int(input())

p = {}
for i in range(n) :
    a, b = map(int, input().split())
    if a not in p :
        p[a] = {}
    if b not in p[a] :
        p[a][b] = 1
    else :
        p[a][b] += 1

ans = 0
for v in p:
    tot, sum = 0,0
    for e in p[v] :
        x = p[v][e]
        sum += x * (x-1)//2
        tot += x
    tot = tot*(tot-1)//2 - sum
    ans += tot

print(ans)