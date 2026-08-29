import sys

n, q = map(int, input().split())
D = [0] + list(map(int, input().split()))
T = [int(input()) for _ in range(q)]


# BIT 1-indexed, initial 1 for alive
bit = [0] * (n + 1)
for i in range(1, n + 1):
    bit[i] += 1
    j = i + (i & -i)
    if j <= n:
        bit[j] += bit[i]

m = n
# precompute highest power of two
pw0 = 1 << (n.bit_length())

out = []
# local variables for speed
bit_local = bit
D_local = D
n_local = n

for tj in T:
    if tj > m:
        out.append(str(m))
    else:
        # find kth
        k = tj
        idx = 0
        pw = pw0
        bl = bit_local
        while pw:
            nxt = idx + pw
            if nxt <= n_local and bl[nxt] < k:
                k -= bl[nxt]
                idx = nxt
            pw >>= 1
        pos = idx + 1
        D_local[pos] -= 1
        if D_local[pos] == 0:
            # remove
            i = pos
            while i <= n_local:
                bl[i] -= 1
                i += i & -i
            m -= 1
        out.append(str(m))

print("\n".join(out))
