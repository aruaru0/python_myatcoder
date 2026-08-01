n, k = map(int, input().split())

g = []
for _ in range(n) :
    x = list(map(int, input().split()))
    c, m, p = x[0], x[1], x[2:]
    g.append(sum(p)-c)

g.sort(reverse=True)

tot = 0
for i in range(k):
    if g[i] < 0 :
        break
    tot += g[i]

print(tot)