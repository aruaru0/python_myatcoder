n, q = map(int, input().split())

# 同じ値 X ごとに区間を集める
seg = [[] for _ in range(q + 1)]
for _ in range(q):
    l, r, x = map(int, input().split())
    seg[x].append((l, r))

# 各 X の区間をソートして重なりを統合し、差分配列に反映
dif = [0] * (n + 2)
for x in range(1, q + 1):
    itv = seg[x]
    if not itv:
        continue
    itv.sort()
    cl, cr = itv[0]
    for l, r in itv[1:]:
        if l <= cr + 1:
            if r > cr:
                cr = r
        else:
            dif[cl] += 1
            dif[cr + 1] -= 1
            cl, cr = l, r
    dif[cl] += 1
    dif[cr + 1] -= 1

# 累積和で各位置の答え
ans = []
cur = 0
for i in range(1, n + 1):
    cur += dif[i]
    ans.append(cur)

print(*ans)
