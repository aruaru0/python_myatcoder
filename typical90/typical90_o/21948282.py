# Contest ID: typical90
# Problem ID: typical90_o ( https://atcoder.jp/contests/typical90/tasks/typical90_o )
# Title: 015. Don't be too close（★6）
# Language: Python (3.8.2)
# Submitted: 2021-04-22 09:17:20 +0000 UTC ( https://atcoder.jp/contests/typical90/submissions/21948282 ) 

N = int(input())

mod = 10**9+7
n = 110000

fact = [0 for _ in range(n+1)]
ifact = [0 for _ in range(n + 1)]

# 階乗
fact[0] = 1
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i % mod

# 階乗のmodPの逆元
ifact[n] = pow(fact[i], mod-2, mod)
for i in range(n, 0, -1):
    ifact[i-1] = ifact[i] * i % mod


def nCr(n, r):
    if n < r or n < r:
        return 0
    #　nCk = n! / (k!(n-k)!)
    ret = fact[n] * ifact[r] % mod
    ret = ret * ifact[n - r] % mod
    return ret


for K in range(1, N+1):
    tot = 0
    for i in range(1, N // K + 2):
        n = N - (K - 1) * (i - 1)
        r = i
        # print(n, r)
        tot += nCr(n, r)
        tot %= mod

    print(tot)
