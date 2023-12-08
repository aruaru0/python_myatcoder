N = int(input())

a = list(map(int, input().split()))

m = set()
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            m.add(a[i]*a[j]*a[k])

print(len(m))