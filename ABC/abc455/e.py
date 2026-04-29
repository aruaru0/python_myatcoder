import sys
from collections import Counter

n = int(input())
s = input().strip()

dab = [0] * (n + 1)
dbc = [0] * (n + 1)
dac = [0] * (n + 1)

ca, cb, cc = 0, 0, 0
for i, ch in enumerate(s):
    if ch == 'A': ca += 1
    elif ch == 'B': cb += 1
    else: cc += 1
    dab[i+1] = ca - cb
    dbc[i+1] = cb - cc
    dac[i+1] = ca - cc

def count_pairs(arr):
    c = Counter(arr)
    r = 0
    for x in c.values():
        r += x * (x - 1) // 2
    return r

pc = Counter(zip(dab, dbc))
kv = 0
for x in pc.values():
    kv += x * (x - 1) // 2

av = count_pairs(dab)
bv = count_pairs(dbc)
cv = count_pairs(dac)

tot = n * (n + 1) // 2
bad = av + bv + cv - 2 * kv
print(tot - bad)

