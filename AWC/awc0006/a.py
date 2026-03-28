n,l, w = map(int, input().split())
d = list(map(int, input().split()))


ans = 0
for i in range(n):
    if l-w <= d[i] <= l+w:
        ans += 1

print(ans)