MOD = 998244353

N, D = map(int, input().split())
A = list(map(int, input().split()))

a = sorted(A)

fact = [1] * (N + 1)
for i in range(2, N + 1):
    fact[i] = fact[i - 1] * i % MOD

ans = 1
l = 0 

for i in range(N):
    while a[l] < a[i] - D:
                l += 1
    cnt = i - l + 1   
    ans = ans * cnt % MOD

den = 1
cnt_eq = 1     
for i in range(1, N):
    if a[i] == a[i - 1]:
        cnt_eq += 1
    else:
        den = den * fact[cnt_eq] % MOD
        cnt_eq = 1
den = den * fact[cnt_eq] % MOD  

ans = ans * pow(den, MOD - 2, MOD) % MOD
print(ans)
