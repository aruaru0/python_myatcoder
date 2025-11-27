import sys

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    # ---- 必要条件 1 : 重複なし ----------
    if len(set(x)) != n or len(set(y)) != m:
        print('No')
        continue

    g = max(x)
    if max(y) != g:                 # 必要条件 2
        print('No')
        continue

    nm = n * m

    # ---- 条件 (1) のチェック ----------
    fx = [0] * (nm + 2)
    fy = [0] * (nm + 2)
    for v in x:
        fx[v] = 1
    for v in y:
        fy[v] = 1

    cx = [0] * (nm + 2)   # X > k の個数
    cy = [0] * (nm + 2)   # Y > k の個数
    for k in range(nm - 1, -1, -1):
        cx[k] = cx[k + 1] + fx[k + 1]
        cy[k] = cy[k + 1] + fy[k + 1]

    ok = True
    for k in range(1, nm + 1):
        cells = nm - cx[k] * cy[k]          # bound ≤ k のセル数
        if cells > k:
            ok = False
            break
    if not ok:
        print('No')
        continue

    # ---- 構成 -------------------------------------------------
    rx = {v: i for i, v in enumerate(x)}   # value → 行
    ry = {v: j for j, v in enumerate(y)}   # value → 列
    s = set(x) & set(y)                     # 共通部分

    a = [[0] * m for _ in range(n)]

    # 1) 共通部分 (G も含む)
    for v in s:
        i, j = rx[v], ry[v]
        a[i][j] = v

    r0, c0 = rx[g], ry[g]

    # 2) 行だけの最大
    for i, v in enumerate(x):
        if v not in s:          # X[i] が Y に無い
            a[i][c0] = v

    # 3) 列だけの最大
    for j, v in enumerate(y):
        if v not in s:
            a[r0][j] = v

    # ---- 残りの数と空きセル ----------
    used = [False] * (nm + 1)
    for v in x:
        used[v] = True
    for v in y:
        used[v] = True

    rest = [v for v in range(1, nm + 1) if not used[v]]

    emp = []                     # (上界 , i , j)
    for i in range(n):
        xi = x[i]
        for j in range(m):
            if a[i][j] == 0:
                bnd = xi if xi < y[j] else y[j]
                emp.append((bnd, i, j))
    emp.sort(key=lambda z: z[0])

    ok2 = True
    for (bnd, i, j), v in zip(emp, rest):
        if v > bnd:
            ok2 = False
            break
        a[i][j] = v

    if not ok2:
        print('No')
        continue

    # ---- 出力 -------------------------------------------------
    print('Yes')
    out = [' '.join(map(str, row)) for row in a]
    print('\n'.join(out))
