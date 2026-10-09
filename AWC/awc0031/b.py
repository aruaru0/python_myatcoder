n, t = map(int, input().split())

ans = 0
for _ in range(t) :
    s = list(map(int, input().split()))
    s.sort(reverse=True)
    if s[0] >= s[1] * 2:
        ans += 1

print(ans)