n, m, k = map(int, input().split())

s = list(map(int, input().split()))

for _ in range(m):
    p, v = map(int, input().split())
    s[p - 1] = v

count = 0
for i in range(n):
    if s[i] < k:
        count += 1

print(count)

