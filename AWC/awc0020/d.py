n, L = map(int, input().split())

p = []
for _ in range(n) :
    x, r = map(int, input().split())
    p.append((x-r, x+r))

p.sort()


cur = 0
ok = True

for l, r in p :
    if cur < l :
        ok = False
        break
    cur = max(cur, r)

if cur < L :
    ok = False

print("Yes" if ok else "No")
