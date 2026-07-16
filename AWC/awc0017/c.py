n, q = map(int, input().split())

c = list(map(int, input().split()))
a = [0]*n
for i in range(n-1):
    if c[i] == c[i+1] :
        a[i+1] = 1

for i in range(1, n) :
    a[i] += a[i-1]


for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(a[r]-a[l])