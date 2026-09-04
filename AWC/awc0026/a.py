n, k = map(int, input().split())
a = list(map(int, input().split()))

b = []
for i in range(n) :
    if (i+1)%k == 0 :
        b.append(a[i])

print(*b)