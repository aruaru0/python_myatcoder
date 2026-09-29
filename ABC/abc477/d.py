n, q = map(int, input().split())

# col[i]: 保存済みの色, tm[i]: その色が有効な最後の時刻
col = ['a'] * (n + 1)
tm = [-1] * (n + 1)
tl = bytearray(n + 1)  # タイルの有無
gt = -1   # 最後の type-2 の時刻
gc = 'a'  # そのときの色
INF = q + 1

for t in range(1, q + 1):
    p = input().split()
    if p[0] == '1':
        x = int(p[1])
        if tl[x]:
            # タイルを外す: 色は凍結したまま、以降の type-2 に従う
            tl[x] = 0
            tm[x] = t
        else:
            # タイルを置く: 現時点の色で凍結
            tl[x] = 1
            if gt > tm[x]:
                col[x] = gc
            tm[x] = INF
    else:
        gt = t
        gc = p[1]

res = [gc if gt > tm[i] else col[i] for i in range(1, n + 1)]
print(''.join(res))
