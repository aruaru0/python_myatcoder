n = int(input())
a = list(map(int, input().split()))

ans = 1
cnt = [0] * (n + 1)
tot = 0 
for i in range(n - 1, -1, -1):
    ans += tot - cnt[a[i]]
    if i == n - 1 or a[i] != a[i + 1]:
        cnt[a[i]] += 1
        tot += 1

print(ans)
