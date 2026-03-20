from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(int)
d[0] = 1
cur = 0
ans = 0

for x in A:
    cur += x
    
    ans += d[cur - K]    
    d[cur] += 1

print(ans)
