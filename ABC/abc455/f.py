import sys
sys.setrecursionlimit(200000)

P = 998244353
INV2 = (P + 1) // 2

N, Q = map(int, input().split())
sz = 4 * N + 1
S1 = [0] * sz
S2 = [0] * sz
LZ = [0] * sz

def push(nd, l, r):
    v = LZ[nd]
    if v == 0:
        return
    m = (l + r) // 2
    # 左子ノード
    ln = m - l + 1
    v1 = S1[2*nd]
    S2[2*nd] = (S2[2*nd] + 2*v*v1 + v*v*ln) % P
    S1[2*nd] = (v1 + v*ln) % P
    LZ[2*nd] = (LZ[2*nd] + v) % P
    # 右子ノード
    rm = r - m
    v2 = S1[2*nd+1]
    S2[2*nd+1] = (S2[2*nd+1] + 2*v*v2 + v*v*rm) % P
    S1[2*nd+1] = (v2 + v*rm) % P
    LZ[2*nd+1] = (LZ[2*nd+1] + v) % P
    LZ[nd] = 0

def update(nd, l, r, ql, qr, val):
    if ql <= l and r <= qr:
        v = val
        S2[nd] = (S2[nd] + 2*v*S1[nd] + v*v*(r-l+1)) % P
        S1[nd] = (S1[nd] + v*(r-l+1)) % P
        LZ[nd] = (LZ[nd] + v) % P
        return
    push(nd, l, r)
    m = (l + r) // 2
    if ql <= m:
        update(2*nd, l, m, ql, qr, val)
    if qr > m:
        update(2*nd+1, m+1, r, ql, qr, val)
    S1[nd] = (S1[2*nd] + S1[2*nd+1]) % P
    S2[nd] = (S2[2*nd] + S2[2*nd+1]) % P

def query(nd, l, r, ql, qr):
    if ql <= l and r <= qr:
        return S1[nd], S2[nd]
    push(nd, l, r)
    m = (l + r) // 2
    r1, r2 = 0, 0
    if ql <= m:
        a, b = query(2*nd, l, m, ql, qr)
        r1 = (r1 + a) % P
        r2 = (r2 + b) % P
    if qr > m:
        a, b = query(2*nd+1, m+1, r, ql, qr)
        r1 = (r1 + a) % P
        r2 = (r2 + b) % P
    return r1, r2

res = []
for _ in range(Q):
    l, r, a = map(int, input().split())
    update(1, 1, N, l, r, a)
    s1, s2 = query(1, 1, N, l, r)
    ans = (s1*s1 - s2) % P
    ans = (ans * INV2) % P
    res.append(str(ans))
print('\n'.join(res))

