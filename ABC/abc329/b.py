N = int(input())
a = list(map(int, input().split()))

a.sort()
v = a[-1]
for i in range(N-1, -1, -1):
    if v != a[i] :
        print(a[i])
        break

