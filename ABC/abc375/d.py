s = input()

n = len(s)
l = [0]*26
r = [0]*26

for i in range(n):
    r[ord(s[i]) - ord('A')] += 1

ans = 0
for i in range(n):
    r[ord(s[i]) - ord('A')] -= 1
    ans += sum(x*y for x, y in zip(l, r))
    l[ord(s[i]) - ord('A')] += 1

print(ans)