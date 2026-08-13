import sys
from collections import defaultdict, Counter

MOD = 998244353
INV2 = (MOD + 1) // 2


def main():
    inp = sys.stdin.readline
    n, m = map(int, inp().split())
    s = inp().strip()

    par = list(range(n))
    sz = [1] * n

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return
        if sz[a] < sz[b]:
            a, b = b, a
        par[b] = a
        sz[a] += sz[b]

    for _ in range(m):
        a, b = map(int, inp().split())
        union(a - 1, b - 1)

    comp = defaultdict(list)
    for i in range(n):
        comp[find(i)].append(i)

    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv = [1] * (n + 1)
    inv[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        inv[i - 1] = inv[i] * i % MOD

    ans = 1
    free = False
    st = 1
    dcnt = 0
    for vs in comp.values():
        k = len(vs)
        if k == 1:
            continue
        cnt = Counter(s[i] for i in vs)
        if max(cnt.values()) >= 2:
            free = True
            a = fact[k]
            for c in cnt.values():
                a = a * inv[c] % MOD
            ans = ans * a % MOD
        else:
            dcnt += 1
            st = st * fact[k] % MOD

    if dcnt > 0:
        ans = ans * st % MOD
        if not free:
            ans = ans * INV2 % MOD

    print(ans % MOD)


main()
