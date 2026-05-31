n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

i = 0
j = 0
ans = 0

while i < n and j < m:
    if b[j] <= 2 * a[i]:
        ans += 1
        i += 1
        j += 1
    else:
        i += 1

print(ans)
