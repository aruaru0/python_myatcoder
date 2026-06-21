n, x = input().split()
idx = ord(x) - ord('A')
ok = False

n = int(n)
for _ in range(n):
    s = input()
    if s[idx] == 'o':
        ok = True
print("Yes" if ok else "No")
