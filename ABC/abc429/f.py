import sys

INF = 10 ** 9
N = int(input())
s0 = input().strip()
s1 = input().strip()
s2 = input().strip()

# 列ごとの mask (bit0:上, bit1:中, bit2:下)
cM = [0] * N
for i in range(N):
    m = 0
    if s0[i] == '.':
        m |= 1 << 0
    if s1[i] == '.':
        m |= 1 << 1
    if s2[i] == '.':
        m |= 1 << 2
    cM[i] = m

# mask (0..7) に対する 3×3 の内部距離行列
lDP = [[INF] * 9 for _ in range(8)]
for m in range(8):
    arr = [INF] * 9
    for a in range(3):
        if not (m >> a) & 1:
            continue
        for b in range(3):
            if not (m >> b) & 1:
                continue
            lo = a if a < b else b
            hi = b if a < b else a
            ok = True
            for k in range(lo, hi + 1):
                if not (m >> k) & 1:
                    ok = False
                    break
            if ok:
                arr[a * 3 + b] = abs(a - b)
    lDP[m] = arr

# セグ木用配列（最大 4N 個のノード）
sz = 4 * N + 5
dpA = [INF] * (sz * 9)   # フラットに 3×3 行列を格納
lm = [0] * sz            # 左端列 mask
rm = [0] * sz            # 右端列 mask

def setl(i, m):
    """葉 i に mask m を設定"""
    bs = i * 9
    arr = lDP[m]
    for t in range(9):
        dpA[bs + t] = arr[t]
    lm[i] = m
    rm[i] = m

sys.setrecursionlimit(1 << 25)

def bld(i, l, r):
    """区間 [l,r] のノード i を構築"""
    if l == r:
        setl(i, cM[l])
    else:
        mid = (l + r) // 2
        lc = i * 2
        rc = lc + 1
        bld(lc, l, mid)
        bld(rc, mid + 1, r)
        mrg(i, lc, rc)

def mrg(p, cl, cr):
    """子 cl , cr を結合してノード p を作る"""
    bs = p * 9
    lbs = cl * 9
    rbs = cr * 9
    crs = rm[cl] & lm[cr]          # 境界で同時に空いている行のビットマスク

    for a in range(3):
        ao = a * 3
        for b in range(3):
            best = INF
            if crs:
                # 行 0
                if crs & 1:
                    v = dpA[lbs + ao + 0]
                    if v < INF:
                        w = dpA[rbs + 0 * 3 + b]
                        if w < INF:
                            cand = v + 1 + w
                            if cand < best:
                                best = cand
                # 行 1
                if crs & 2:
                    v = dpA[lbs + ao + 1]
                    if v < INF:
                        w = dpA[rbs + 1 * 3 + b]
                        if w < INF:
                            cand = v + 1 + w
                            if cand < best:
                                best = cand
                # 行 2
                if crs & 4:
                    v = dpA[lbs + ao + 2]
                    if v < INF:
                        w = dpA[rbs + 2 * 3 + b]
                        if w < INF:
                            cand = v + 1 + w
                            if cand < best:
                                best = cand
            dpA[bs + ao + b] = best

    lm[p] = lm[cl]
    rm[p] = rm[cr]

# 初期構築
bld(1, 0, N - 1)

Q = int(input())
out = []
for _ in range(Q):
    r, c = map(int, input().split())
    r -= 1
    c -= 1

    # ビット反転
    cM[c] ^= (1 << r)

    # 葉の更新 + 上方へ伝搬
    i = 1
    l = 0
    rr = N - 1
    while True:
        if l == rr:
            setl(i, cM[c])
            break
        mid = (l + rr) // 2
        if c <= mid:
            i = i * 2
            rr = mid
        else:
            i = i * 2 + 1
            l = mid + 1

    while i > 1:
        p = i // 2
        mrg(p, p * 2, p * 2 + 1)
        i = p

    ans = dpA[9 + 2]          # root (idx=1) の [0][2]
    out.append("-1" if ans >= INF else str(ans))

print("\n".join(out))


