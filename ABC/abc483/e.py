n, m = map(int, input().split())

pw = [1] * m
for i in range(1, m):
    pw[i] = pw[i - 1] * 27

cnt = {}
for _ in range(n):
    s = input().strip()
    c = 0
    for i in range(m):
        c += (ord(s[i]) - 96) * pw[i]
    cnt[c] = cnt.get(c, 0) + 1

n0 = 0
for v in cnt.values():
    n0 += v * (v - 1) // 2

it = list(cnt.items())

s1 = 0
for p in range(m):
    pp = pw[p]
    d = {}
    t = 0
    for code, c in it:
        key = code - ((code // pp) % 27) * pp
        old = d.get(key, 0)
        t += old * c + c * (c - 1) // 2
        d[key] = old + c
    s1 += t

s2 = 0
for p in range(m):
    pp = pw[p]
    for q in range(p + 1, m):
        qq = pw[q]
        d = {}
        t = 0
        for code, c in it:
            key = code - ((code // pp) % 27) * pp - ((code // qq) % 27) * qq
            old = d.get(key, 0)
            t += old * c + c * (c - 1) // 2
            d[key] = old + c
        s2 += t

n1 = s1 - m * n0
n2 = s2 - (m * (m - 1) // 2) * n0 - (m - 1) * n1
print(n0 + n1 + n2)
