# --------------- BIT -----------------
def add(b, i, v):
    # i : 1-indexed
    while i < len(b):
        b[i] += v
        i += i & -i

def pref(b, i):
    s = 0
    while i:
        s += b[i]
        i -= i & -i
    return s
# -----------------------------------

MAXV = 500100
SIZE = MAXV

n, q = map(int, input().split())
a = list(map(int, input().split()))

bitC = [0] * SIZE        # 出現回数
bitS = [0] * SIZE        # 総和

# 初期配列の登録
for v in a:
    idx = v + 1          # 0 を 1 にマッピング
    add(bitC, idx, 1)
    add(bitS, idx, v)

out_lines = []
for _ in range(q):
    tmp = input().split()
    t = int(tmp[0])
    if t == 1:
        x = int(tmp[1]) - 1
        y = int(tmp[2])
        old = a[x]
        if old != y:
            idx = old + 1
            add(bitC, idx, -1)
            add(bitS, idx, -old)
            idx = y + 1
            add(bitC, idx, 1)
            add(bitS, idx, y)
            a[x] = y
    else:
        l = int(tmp[1])
        r = int(tmp[2])
        if l > r:
            ans = n * l
        else:
            if l == 0:
                cntL = 0
                sumL = 0
            else:
                iL = l          # (l-1)+1
                cntL = pref(bitC, iL)
                sumL = pref(bitS, iL)

            iR = r + 1
            cntR = pref(bitC, iR)
            sumR = pref(bitS, iR)

            low = cntL
            mid = sumR - sumL
            high = n - cntR
            ans = l * low + mid + r * high

        print(ans)
