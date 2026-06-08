from collections import defaultdict


n, k, m = map(int, input().split())
col = defaultdict(list)

for _ in range(n):
    c, v = map(int, input().split())
    col[c - 1].append(v)

for c in col:
    col[c].sort(reverse=True)

gem = []
for c, vs in col.items():
    for v in vs:
        gem.append((v, c))

gem.sort(reverse=True)

sel = gem[:k]
tot = sum(v for v, _ in sel)

cnt = defaultdict(int)
for v, c in sel:
    cnt[c] += 1

if len(cnt) >= m:
    print(tot)
    exit()

rem = []
for c, cn in cnt.items():
    for i in range(1, cn):
        rem.append(col[c][i])

add = []
for c, vs in col.items():
    if c not in cnt:
        add.append(vs[0])

rem.sort()
add.sort(reverse=True)

nd = m - len(cnt)
ans = tot - sum(rem[:nd]) + sum(add[:nd])
print(ans)
