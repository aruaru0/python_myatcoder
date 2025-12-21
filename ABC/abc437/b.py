h, w, n = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(h)]
b = set([int(input()) for _ in range(n)])

ans = 0
for r in range(h) :
    tot = 0
    for c in range(w) :
        if a[r][c] in b :
            tot += 1
    ans = max(ans, tot)


print(ans)