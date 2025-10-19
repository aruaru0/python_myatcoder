
n, k = map(int, input().split())
s = input().strip()

d = {}                     # 出現回数を記録
for i in range(n - k + 1):
    t = s[i:i + k]
    d[t] = d.get(t, 0) + 1

mx = max(d.values()) if d else 0
ans = [t for t, cnt in d.items() if cnt == mx]
ans.sort()

print(mx)
print(' '.join(ans))

