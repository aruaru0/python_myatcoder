MOD = 998244353

n = int(input())
A = list(map(int, input().split()))

m = n + 2
inv = [0] * (m + 1)
inv[1] = 1
for i in range(2, m + 1):
    inv[i] = MOD - MOD // i * inv[MOD % i] % MOD

H = [0] * (m + 1)
for k in range(1, m + 1):
    H[k] = (H[k - 1] + inv[k]) % MOD

PH = [0] * (m + 2)
for k in range(0, m + 1):
    PH[k + 1] = (PH[k] + H[k]) % MOD

ans = 0
for i in range(1, n + 1):
    ci = (PH[n + 1] - PH[n - i + 1] - PH[i]) % MOD
    ans = (ans + A[i - 1] * ci) % MOD

print(ans)