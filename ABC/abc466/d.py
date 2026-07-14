n, m = map(int, input().split())
ops = [tuple(map(int, input().split())) for _ in range(m)]

used_rows = set()
used_cols = set()
ans = 0

for r, c in reversed(ops):
    if r not in used_rows and c not in used_cols:
        ans += 1
    used_rows.add(r)
    used_cols.add(c)

print(ans)
