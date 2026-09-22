import sys

def read_n(n):
    a = []
    while len(a) < n:
        a.extend(map(int, input().split()))
    return a[:n]

N, M, K = map(int, input().split())
X, Y = map(int, input().split())
A = sorted(read_n(N))
B = sorted(read_n(M))

W = X + K * Y

# 累積和
PA = [0] * (N + 1)
for i in range(N):
    PA[i + 1] = PA[i] + A[i]

PB = [0] * (M + 1)
PC = [0] * (M + 1)
for j in range(M):
    PB[j + 1] = PB[j] + B[j]
    PC[j + 1] = PC[j] + (B[j] + K - 1) // K

ans = 0
for t in range(M + 1):
    if PC[t] > Y or PB[t] > W:
        break
    rem = W - PB[t]
    # 残り予算で買えるデザートの最大数（PA は狭義単調増加）
    lo, hi = 0, N
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if PA[mid] <= rem:
            lo = mid
        else:
            hi = mid - 1
    if t + lo > ans:
        ans = t + lo

print(ans)
