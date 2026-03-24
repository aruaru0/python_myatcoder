from collections import deque

n, k = map(int, input().split())

a = list(map(int, input().split()))
a = [x%k for x in a]
a.sort()

a = deque(a)

ans = k
for i in range(n):
    ans = min(ans, a[-1] - a[0])
    a.append(a.popleft()+k)

print(ans)