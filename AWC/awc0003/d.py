import bisect
n, k, m = map(int, input().split())

a = list(map(int, input().split()))

b = [0] * (n+1)
for i in range(n) :
    b[i+1] = b[i] + a[i]

cnt = 0
for i in range(0, n-k+1) :
    d = b[i] + m
    pos = bisect.bisect_left(b, d)
    pos = max(i+k, pos)
    cnt += n - pos + 1

print(cnt)