n = int(input())

# 差分配列の準備 (N+2サイズで範囲外参照を防ぐ)
da = [0] * (n + 2)
db = [0] * (n + 2)
dt = [0] * (n + 2)

for _ in range(n):
    li, ri = map(int, input().split())
    
    # チームAの条件: k is in [li, ri]
    da[li] += 1
    if ri + 1 <= n:
        da[ri+1] -= 1
    
    # チームBの条件: N-k is in [li, ri] => k is in [n-ri, n-li]
    bi = n - ri
    ei = n - li
    db[bi] += 1
    if ei + 1 <= n:
        db[ei+1] -= 1
        
    # 両方の条件を満たす範囲 (Intersection)
    st = max(li, bi)
    en = min(ri, ei)
    if st <= en:
        dt[st] += 1
        if en + 1 <= n:
            dt[en+1] -= 1

mod = 998244353

# 階乗と逆元の事前計算 (nCr用)
fac = [1] * (n + 1)
inv = [1] * (n + 1)
for i in range(1, n + 1):
    fac[i] = (fac[i-1] * i) % mod
inv[n] = pow(fac[n], mod - 2, mod)
for i in range(n - 1, -1, -1):
    inv[i] = (inv[i+1] * (i + 1)) % mod

def nCr(nn, rr):
    if rr < 0 or rr > nn:
        return 0
    num = fac[nn]
    den = (inv[rr] * inv[nn-rr]) % mod
    return (num * den) % mod

ans = 0
ca = 0 # count A
cb = 0 # count B
ct = 0 # count both

# k=1 から N-1 まで走査
for k in range(1, n):
    # 差分配列を累積させて現在の個数を取得
    ca += da[k]
    cb += db[k]
    ct += dt[k]
    
    # 全員が A または B の条件を満たしているかチェック
    # |A union B| = |A| + |B| - |A intersect B|
    if ca + cb - ct == n:
        # 必須のA人数 (n_A) = count(A only) = ca - ct
        na = ca - ct
        # どちらでもよい人数 (n_both) = ct
        # チームAにあと何人入れる必要があるか = k - na
        ans = (ans + nCr(ct, k - na)) % mod

print(ans)

