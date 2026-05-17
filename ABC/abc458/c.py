s = input()
n = len(s)

cnt = 0
for i in range(n):
    if s[i] == 'C':
        cnt += min(i, n-1-i)+1

print(cnt)