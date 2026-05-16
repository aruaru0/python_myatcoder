n, k, m = map(int, input().split())
ex = []
bg = []
for _ in range(n):
    h, p = map(int, input().split())
    if h == 1:
        ex.append(p)
    else:
        bg.append(p)
ex.sort(reverse=True)
bg.sort(reverse=True)
if len(ex) < m or len(bg) < k - m:
    print(-1)
    exit()
ans = sum(ex[:m]) + sum(bg[:k - m])
print(ans)
