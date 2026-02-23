from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

m = defaultdict(int)
for i in range(n):
    m[a[i]] = max(m[a[i]], m[a[i]-1]+1)

print(max(m.values()))