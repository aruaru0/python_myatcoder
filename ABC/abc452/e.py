


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

MOD = 998244353

P = [0] * (N + 1)
sum_ia = 0
for i in range(1, N + 1):
    val = A[i-1]
    P[i] = P[i-1] + val
    sum_ia = (sum_ia + i * val) % MOD

sum_b = sum(B) % MOD
s1 = (sum_ia * sum_b) % MOD

s2 = 0
limit_j = min(N, M)

for j in range(1, limit_j + 1):
    tj = 0
    for start in range(j, N + 1, j):
        k = start // j
        end = min(N, start + j - 1)
        sum_range = P[end] - P[start-1]
        tj += k * sum_range
    
    term_s2 = (B[j-1] * j * (tj % MOD)) % MOD
    s2 = (s2 + term_s2) % MOD

ans = (s1 - s2 + MOD) % MOD
print(ans)

