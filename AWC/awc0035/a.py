n, m = map(int, input().split())
p = list(map(int, input().split()))


d= [0] * n
for _ in range(m) :
    u, v, w = map(int, input().split())
    u-=1
    v-=1
    d[u] -= w
    d[v] += w


for i in range(n) :
    p[i] += d[i]


ans = 0
for i in range(n) :
    if p[ans] < p[i] :
        ans = i

print(ans+1)