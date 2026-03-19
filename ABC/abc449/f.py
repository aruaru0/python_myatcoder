import sys

# セグメント木の深い再帰に対応するため上限を引き上げ
sys.setrecursionlimit(300000)

data = input().split()
H = int(data[0])
W = int(data[1])
h = int(data[2])
w = int(data[3])
N = int(data[4])

mr = H - h + 1
mc = W - w + 1
if mr <= 0 or mc <= 0:
    print(0)
    exit()

ev = []
for _ in range(N):
    line = input().split()
    R = int(line[0])
    C = int(line[1])
    lr = max(1, R - h + 1)
    ur = min(R, mr)
    lc = max(1, C - w + 1)
    uc = min(C, mc)
    if lr <= ur and lc <= uc:
        # 矩形の左端と右端のイベントを登録
        ev.append((lr, 1, lc, uc))
        ev.append((ur + 1, -1, lc, uc))

ys = [1, mc + 1]
for e in ev:
    y1 = e[2]
    y2 = e[3]
    ys.append(y1)
    ys.append(y2 + 1)

# 座標圧縮
ys = sorted(set(ys))
sz = len(ys)

cnt = [0] * (4 * sz)
ln = [0] * (4 * sz)

# セグメント木の初期化
def b(idx, l, r):
    if r - l <= 1:
        cnt[idx] = 0
        ln[idx] = 0
    else:
        mid = (l + r) // 2
        b(2 * idx + 1, l, mid)
        b(2 * idx + 2, mid, r)
        ln[idx] = 0
        
# インデックスは 0 から sz - 1 まで
b(0, 0, sz - 1)

# セグメント木の更新
def u(idx, l, r, ql, qr, delta):
    # l, r を実際の座標 ys[l], ys[r] に変換して比較する
    if qr <= ys[l] or ql >= ys[r]:
        return
    if ql <= ys[l] and ys[r] <= qr:
        cnt[idx] += delta
        if cnt[idx] > 0:
            ln[idx] = ys[r] - ys[l]
        else:
            if r - l == 1:
                ln[idx] = 0
            else:
                ln[idx] = ln[2 * idx + 1] + ln[2 * idx + 2]
        return
        
    mid = (l + r) // 2
    u(2 * idx + 1, l, mid, ql, qr, delta)
    u(2 * idx + 2, mid, r, ql, qr, delta)
    
    if cnt[idx] > 0:
        ln[idx] = ys[r] - ys[l]
    else:
        if r - l == 1:
            ln[idx] = 0
        else:
            ln[idx] = ln[2 * idx + 1] + ln[2 * idx + 2]

# 平面走査 (Sweep Line)
ev.sort()
px = 1
area = 0
i = 0
while i < len(ev):
    x = ev[i][0]
    if px < x:
        area += ln[0] * (x - px)
        px = x
    while i < len(ev) and ev[i][0] == x:
        typ = ev[i][1]
        y1 = ev[i][2]
        y2 = ev[i][3]
        # y1, y2+1 を更新 (区間は sz - 1 まで)
        u(0, 0, sz - 1, y1, y2 + 1, typ)
        i += 1
        
ans = mr * mc - area
print(ans)
