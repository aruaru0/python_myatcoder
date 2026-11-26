import sys

W = 40
LOW = 39
LANE = (1 << 40) - 1

n, m = map(int, input().split())
grp = {}
tot = 0
for _ in range(n):
    c, v = map(int, input().split())
    grp.setdefault(c, []).append(v)
    tot += v

nl = m + 1
FULL = (1 << (W * nl)) - 1
REP = FULL // LANE    
H = REP << LOW   
A = [0] * (n + 1)
ans = [0] * nl
cur = tot
ans[m] = cur
cnt = 0
anchor = m


def fill(G):
    best = [0] * (G + 1)
    for k in range(cnt + 1):
        pk = m - k
        if pk < 0:
            continue
        pmin = m - k * G
        lo = pmin if pmin > 0 else 0
        span = pk - lo + 1
        chunk = (A[k] >> (W * lo)) & ((1 << (W * span)) - 1)
        b = chunk.to_bytes(span * 5, 'little')
        tmax = m // k if k else G
        if tmax > G:
            tmax = G
        idx = pk - lo
        for t in range(1, tmax + 1):
            val = int.from_bytes(b[idx * 5: idx * 5 + 5], 'little')
            if val > best[t]:
                best[t] = val
            idx -= k
    for t in range(1, G + 1):
        ans[anchor - t] = cur + best[t]


for i in sorted(grp.keys(), reverse=True):
    G = anchor - i
    if G > 0:
        fill(G)
        for k in range(1, cnt + 1):
            d = k * G
            if d > m:
                A[k] = 0
            else:
                A[k] = (A[k] << (W * d)) & FULL
        anchor = i
    for v in grp[i]:
        cur -= v
        vc = v * REP
        for k in range(cnt, -1, -1):
            S = A[k] + vc
            Dst = A[k + 1]
            D = (S | H) - Dst
            u = (D & H) >> LOW
            sel = ((u << W) - u) & FULL
            A[k + 1] = (S & sel) | (Dst & (FULL ^ sel))
        cnt += 1

if anchor > 0:
    fill(anchor)

print(*ans, sep='\n')
