import bisect

n = int(input())
H = []
L = []
for _ in range(n):
    h, l = map(int, input().split())
    H.append(h)
    L.append(l)

suf = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    suf[i] = max(H[i], suf[i + 1])

q = int(input())
T = list(map(int, input().split()))
for t in T:
    idx = bisect.bisect_right(L, t)
    print(suf[idx])
