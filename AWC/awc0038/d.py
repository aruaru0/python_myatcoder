MOD = 998244353
N = int(input())
W = map(int, input().split())

# fact, inv_factを計算
m = N - 1
fact = [1] * (m + 1)
for i in range(1, m + 1):
    fact[i] = fact[i - 1] * i % MOD
    
inv_fact = [1] * (m + 1)
inv_fact[m] = pow(fact[m], MOD - 2, MOD)
for i in range(m, 0, -1):
    inv_fact[i - 1] = inv_fact[i] * i % MOD

sum_w = sum(W) % MOD

K = N // 2 + 1
ways = 0
fact_m = fact[m]
for k in range(K, N + 1):
    r = k - 1
    comb = fact_m * inv_fact[r] % MOD * inv_fact[m - r] % MOD
    ways = (ways + comb) % MOD
    
print(sum_w * ways % MOD)

