s = input().strip()
a = sorted(s)

if a[0] != '0':
    ans = ''.join(a)
else:
    i = 0
    while a[i] == '0':
        i += 1
    ans = a[i] + ''.join(a[:i]) + ''.join(a[i+1:])

print(ans)