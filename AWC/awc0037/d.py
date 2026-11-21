n, k = map(int, input().split())


def nCr(n, r, mod) :
    if r < 0 or r > n:
        return 0
    x = 1
    for i in range(1, n+1) :
        x *= i
        x %= mod
    y = 1
    for i in range(1, r+1) :
        y *= i
        y %= mod
    z = 1 
    for i in range(1, n-r+1) :
        z *= i
        z %= mod

    y *= z
    y %= mod
    iy = pow(y, mod-2, mod)
    return (x*iy)%mod
    

p = k + 1
r = n - (2*k-1)

# print(p+r-1, r)
print(nCr(p+r-1, r, 10**9+7))