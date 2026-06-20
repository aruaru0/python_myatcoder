n, k, q = map(int, input().split())

a = list(map(int, input().split()))
p = [0]*(n+1)

r = 0
cnt = 0
for l in range(n) :
    while r < n and cnt <= k :
        cnt += a[r]
        r += 1
    p[l+1] = r
    cnt -= a[l]

for i in range(n):
    p[i+1] += p[i]

for _ in range(q) :
    l, r = map(int, input().split())
    l -= 1
    print(p[r] - p[l])