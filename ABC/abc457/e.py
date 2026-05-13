import bisect
import sys
from bisect import bisect_left

n, m = map(int, input().split())

n_size = n + 2
rs = [[] for _ in range(n_size)]
ls = [[] for _ in range(n_size)]

INF = 1001001001
min_r = [INF] * n_size

for _ in range(m):
    l, r = map(int, input().split())
    rs[l].append(r)
    ls[r].append(l)
    if r < min_r[l]:
        min_r[l] = r
        
# 各リストをソート
for i in range(n_size):
    rs[i].sort()
    ls[i].sort()
    
# minRの累積最小値を後ろから計算
for i in range(n_size - 2, -1, -1):
    if min_r[i+1] < min_r[i]:
        min_r[i] = min_r[i+1]
        
q = int(input())
results = []

for _ in range(q):
    l, r = map(int, input().split())
    
    # solve 内部ロジック
    # lwb(rs[l], r+1) - lwb(rs[l], r) は rs[l] 内にある値 r の個数
    cnt = bisect_left(rs[l], r + 1) - bisect_left(rs[l], r)
    
    found = False
    if cnt > 0:
        # r が rs[l] に含まれる場合
        if min_r[l] < r or (l + 1 < n_size and min_r[l + 1] <= r):
            found = True
        elif cnt >= 2:
            found = True
    else:
        # r が rs[l] に含まれない場合
        ri_idx = bisect_left(rs[l], r) - 1
        li_idx = bisect_left(ls[r], l)
        
        if ri_idx >= 0 and li_idx < len(ls[r]):
            if rs[l][ri_idx] + 1 >= ls[r][li_idx]:
                found = True
    
    results.append("Yes" if found else "No")
    
sys.stdout.write("\n".join(results) + "\n")