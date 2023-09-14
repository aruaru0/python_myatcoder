
class cMod :
    def __init__(self, mod, size):
        fact = [1 for _ in range(size)]
        ifact = [1 for _ in range(size)]

        for i in range(1, size) :
            fact[i] = fact[i-1] * i % mod

        ifact[size-1] = pow(fact[size-1], mod-2, mod)

        for i in range(size-2, -1, -1):
            ifact[i] = ifact[i+1] * (i+1) % mod
        self.fact = fact
        self.ifact = ifact
        self.mod = mod

    def nCk(self, n: int, k: int) -> int:
        if n < k or k < 0 : return 0
        return self.fact[n] * self.ifact[k] % self.mod * self.ifact[n-k]%mod
        
    
mod = 1000000007
size = 210000

m = cMod(mod, size)


X, Y = map(int, input().split())
print(m.nCk(X+Y, X))
