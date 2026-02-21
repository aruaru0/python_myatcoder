n, m = map(int, input().split())
ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a < m:
        diff = m - a
        need = (diff + b - 1) // b
        if need > ans:
            ans = need
print(ans)
