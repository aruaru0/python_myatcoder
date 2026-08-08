from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

dq = deque()
ans = 0
for i in range(n):
    while dq and dq[0] <= i - k:
        dq.popleft()
    if (a[i] + len(dq)) % 2 == 1:
        if i + k > n:
            print(-1)
            exit()
        dq.append(i)
        ans += 1
print(ans)
