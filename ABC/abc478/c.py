from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

pre = [True] * (n + 1)
for i in range(1, n):
    pre[i + 1] = pre[i] and a[i - 1] <= a[i]

suf = [True] * (n + 1)
for i in range(n - 2, -1, -1):
    suf[i] = suf[i + 1] and a[i] <= a[i + 1]

m = n - k + 1
wmin = [0] * m
wmax = [0] * m

dq = deque()
for j in range(n):
    while dq and a[dq[-1]] >= a[j]:
        dq.pop()
    dq.append(j)
    if dq[0] <= j - k:
        dq.popleft()
    if j >= k - 1:
        wmin[j - k + 1] = a[dq[0]]

dq = deque()
for j in range(n):
    while dq and a[dq[-1]] <= a[j]:
        dq.pop()
    dq.append(j)
    if dq[0] <= j - k:
        dq.popleft()
    if j >= k - 1:
        wmax[j - k + 1] = a[dq[0]]

for i in range(m):
    if not pre[i] or not suf[i + k]:
        continue
    if i > 0 and a[i - 1] > wmin[i]:
        continue
    if i + k < n and wmax[i] > a[i + k]:
        continue
    print("Yes")
    break
else:
    print("No")
