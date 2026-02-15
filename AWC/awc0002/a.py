n, k = map(int, input().split())

a = list(map(int, input().split()))

ans = -1
for i in range(n) :
    if a[i] == k :
        ans = i + 1
        break

print(ans)