n = int(input())

a = [0 for _ in range(n)]
b = [0 for _ in range(n)]
c = [0 for _ in range(n)]
for i in range(n):
    a[i], b[i], c[i] = map(int, input().split())
xy = []
for i in range(n):
    for j in range(i + 1, n):
        x = (c[i] * b[j] - c[j] * b[i]) / (a[i] * b[j] - a[j] * b[i])
        y = (c[i] * a[j] - c[j] * a[i]) / (a[j] * b[i] - a[i] * b[j])
        xy.append ([x, y])
ans = 0
for x, y in xy:
    ok = True
    for i in range(n):
        if a[i] * x + b[i] * y > c[i]:
            ok = False
            break
    if ok:       
        ans = max(ans, x + y)
print(ans)
