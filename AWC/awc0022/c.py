n, m, k, t = map(int, input().split())
b = list(map(int, input().split()))

p = [0]*(n+2)
for e in b :
    p[e] = 1

for i in range(n+1) :
    p[i+1] += p[i]


for i in range(k):
    l, r = map(int, input().split())
    if p[r] - p[l-1] >= t :
        print("YES")
    else :
        print("NO")