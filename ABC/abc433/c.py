s = input().strip()
n = len(s)

r = [0] * n
r[n - 1] = 1
for i in range(n - 2, -1, -1):
    if s[i] == s[i + 1]:
        r[i] = r[i + 1] + 1
    else:
        r[i] = 1

ans = 0  
cur = 0
for i in range(n):
    if i == 0 or s[i] != s[i - 1]:
        cur = 1
    else:
        cur += 1

    if i < n - 1 and (ord(s[i]) - 48) + 1 == (ord(s[i + 1]) - 48):
        v = cur if cur <= r[i + 1] else r[i + 1]
        ans += v

print(ans)
