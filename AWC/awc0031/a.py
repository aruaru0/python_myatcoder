n, m, k = map(int, input().split())

p = []
for i in range(n):
    t = list(map(int, input().split()))
    p.append((t[0], i, t[2:]))

p.sort(key=lambda x: (-x[0], x[1]))


cnt = [0] * m

for _, _, t in p[:k] :
    for e in t :
        cnt[e-1] += 1

ans = 0
for i in range(m) :
    if cnt[i] == k :
        ans += 1

print(ans)