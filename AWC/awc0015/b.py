n, k = map(int, input().split())
p = list(map(int, input().split()))

ans = -1
for i in range(n):
    if p[i] >= k :
        ans = i+1
        break

print(ans)