n, m = map(int, input().split())
c = list(map(int, input().split()))


ans = 0
for i in range(m):
    t = int(input()) - 1
    if c[t] != 0:
        c[t] -= 1
        ans += 1

print(ans)