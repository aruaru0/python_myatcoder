from collections import defaultdict

n = int(input())

a = list(map(int, input().split()))
l = defaultdict(int)
r = defaultdict(int)
for i in range(n):
    r[a[i]] += 1

ans = 0
for j in range(n):
    cur = a[j]
    l[cur] += 1
    r[cur] -= 1
    if cur % 5 != 0:
        continue
    k = l[cur / 5 * 3] * l[cur / 5 * 7] + r[cur / 5 * 3] * r[cur / 5 * 7]
    ans += k

print(ans)