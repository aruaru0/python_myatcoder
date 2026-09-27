n, d = map(int, input().split())
x = list(map(int, input().split()))

x = [[e, i]for i, e in enumerate(x)]
inf = int(1e18)
x.append([inf, n])
x.append([-inf, n])

x.sort()


ans = []
for i in range(1, n+1):
    l = x[i][0] - x[i-1][0]
    r = x[i+1][0] - x[i][0]
    if l >= d and r >= d:
        ans.append(x[i][1]+1)


ans.sort()
print(len(ans))
print(*ans)