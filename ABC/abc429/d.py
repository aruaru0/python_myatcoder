n, m, c = map(int, input().split())

a = []
while len(a) < n:
    a += list(map(int, input().split()))

cnt = {}
for v in a:
    cnt[v] = cnt.get(v, 0) + 1


p = sorted(cnt.keys())  
w = [cnt[x] for x in p] 
k = len(p)


w2 = w + w 
r = 0
cur = 0
z = [0] * k  


for i in range(k):
    while cur < c:
        cur += w2[r]
        r += 1
    z[i] = cur
    cur -= w2[i]


if k == 1:
    ans = m * z[0]
else:
    ans = 0
    for i in range(k):
        prev = p[i - 1] if i > 0 else p[-1]
        d = (p[i] - prev) % m        
        ans += d * z[i]

print(ans)

