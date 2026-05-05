S = input()
MOD = 998244353

ca, cb, cc = 0, 0, 0

for c in S:
    if c == 'a':
        ca = (ca + cb + cc + 1) % MOD
    elif c == 'b':
        cb = (cb + ca + cc + 1) % MOD
    elif c == 'c':
        cc = (cc + ca + cb + 1) % MOD

print((ca + cb + cc) % MOD)
