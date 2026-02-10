n = int(input())
a_list = list(map(int, input().split()))
m = max(a_list)
f = [0] * (m + 1)
for v in a_list:
    f[v] += 1

c = [0] * m
suffix = 0
for j in range(m - 1, -1, -1):
    suffix += f[j + 1]
    c[j] = suffix

dlen = m + 20
d = [0] * dlen
for j in range(m):
    d[j] += c[j]

for i in range(dlen - 1):
    carry = d[i] // 10
    d[i] %= 10
    d[i + 1] += carry

idx = dlen - 1
while idx > 0 and d[idx] == 0:
    idx -= 1

out = ''.join(str(d[i]) for i in range(idx, -1, -1))
print(out)

