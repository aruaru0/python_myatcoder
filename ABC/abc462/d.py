N, D = map(int, input().split())
MAX = 10 ** 6 + 5
diff = [0] * (MAX + 2)

for _ in range(N):
    s, t = map(int, input().split())
    if t - D >= s:
        diff[s] += 1
        diff[t - D + 1] -= 1

ans = 0
cnt = 0
for i in range(1, MAX + 1):
    cnt += diff[i]
    ans += cnt * (cnt - 1) // 2

print(ans)
