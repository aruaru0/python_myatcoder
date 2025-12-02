import sys
from array import array

N = int(input())

H = 2000          # 行数
W = 2000          # 列数
w2 = W + 2        # 幅+2（境界用）
sz = (H + 2) * w2

cnt = array('i', [0]) * sz      # 被覆雲の個数（32bit）
sid = array('q', [0]) * sz      # 雲番号総和（64bit）

for i in range(1, N + 1):
    u, d, l, r = map(int, input().split())
    dd = d + 1
    rr = r + 1

    idx = u * w2 + l 
    cnt[idx] += 1
    sid[idx] += i

    idx = u * w2 + rr 
    cnt[idx] -= 1
    sid[idx] -= i

    idx = dd * w2 + l 
    cnt[idx] -= 1
    sid[idx] -= i

    idx = dd * w2 + rr  
    cnt[idx] += 1
    sid[idx] += i

# ---------- 横方向累積和 ----------
for y in range(H + 2):
    base = y * w2
    for x in range(1, w2):
        idx = base + x
        cnt[idx] += cnt[idx - 1]
        sid[idx] += sid[idx - 1]

# ---------- 縦方向累積和 ----------
for y in range(1, H + 2):
    base = y * w2
    prev = (y - 1) * w2
    for x in range(w2):
        idx = base + x
        cnt[idx] += cnt[prev + x]
        sid[idx] += sid[prev + x]

# ---------- 統計 ----------
uni = 0 
exc = [0] * (N + 1)  
tot = H * W 

for y in range(1, H + 1):
    base = y * w2
    for x in range(1, w2 - 1):
        idx = base + x
        c = cnt[idx]
        if c:
            uni += 1
        if c == 1:
            iid = sid[idx] 
            exc[iid] += 1

base_val = tot - uni 
out = []
for i in range(1, N + 1):
    out.append(str(base_val + exc[i]))
print("\n".join(out))
