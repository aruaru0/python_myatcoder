import sys

MOD = 998244353

n, k = map(int, input().split())
a = list(map(int, input().split()))

s1 = sum(a) % MOD
s2 = sum(x * x for x in a) % MOD

# precompute factorials
fac = [1] * (n + 1)
for i in range(1, n + 1):
    fac[i] = fac[i - 1] * i % MOD
ifac = [1] * (n + 1)
ifac[n] = pow(fac[n], MOD - 2, MOD)
for i in range(n, 0, -1):
    ifac[i - 1] = ifac[i] * i % MOD

def comb(a_, b_):
    if b_ < 0 or b_ > a_:
        return 0
    return fac[a_] * ifac[b_] % MOD * ifac[a_ - b_] % MOD

c_pairs = comb(n - 2, k - 2)  # both i,j (i!=j) selected
c_single = comb(n - 1, k - 1)  # single i selected

ans = ((s1 * s1 - s2) % MOD) * c_pairs % MOD
ans = (ans + s2 * c_single) % MOD
print(ans)

