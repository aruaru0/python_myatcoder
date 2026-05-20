MOD = 998244353
X1, X2, X3 = map(int, input().split())

#組み合わせ計算のための前計算
N = X1 + X2 + X3 + 5
fact = [1] * N
finv = [1] * N

for i in range(2, N):
    fact[i] = (fact[i-1] * i) % MOD

finv[N-1] = pow(fact[N-1], MOD-2, MOD)
for i in range(N-2, -1, -1):
    finv[i] = (finv[i+1] * (i+1)) % MOD

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * finv[r] % MOD * finv[n-r] % MOD

ans = 0
limit_i = min(X1 - 1, X2)

for i in range(limit_i + 1):
#各項の計算
    c1 = nCr(X1 - 1, i)
    c2 = nCr(X2 + 1, i + 1)
    c3 = nCr(X2 + X3 - i - 1, X2 - i - 1)
    
    ans = (ans + c1 * c2 % MOD * c3) % MOD

print(ans)
