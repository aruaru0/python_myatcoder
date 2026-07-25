m, d = map(int, input().split())
s = input()

p = [0] * m
for i in range(m):
    if s[i] == 'G' :
        l, r = max(0, i-d), min(m, i+d+1)
        p[l] += 1
        if r != m :
            p[r] -= 1

for i in range(1, m):
    p[i] += p[i-1]

cnt = sum([p[i] == 0 for i in range(m)])

print(cnt)