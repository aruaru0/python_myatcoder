n, m = map(int, input().split())

a = list(map(int, input().split()))
d = list(map(int, input().split()))

a.sort(reverse=True)
d.sort(reverse=True)

ans = 0
j = 0 
for i in range(m):
    if d[i] > a[j] :
        print(-1)
        exit()
    ans += abs(a[j] - d[i])
    j += 1

print(ans)