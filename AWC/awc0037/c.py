n, k = map(int, input().split())

a = list(map(int, input().split()))

mod = int(1e9+7)

tot = 1
for i in range(k) :
    tot *= a[i]
    tot %= mod

def inv(a, p) :
    return pow(a, -1, p)

ans = tot
for i in range(k, n) :
    tot *= inv(a[i-k], mod)
    tot %= mod
    tot *= a[i]
    tot %= mod
    ans += tot
    ans %= mod

print(ans)