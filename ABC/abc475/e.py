tr = str.maketrans('ox', '01')


def toi(s):
    return int(s.translate(tr), 2)


n, m, k = map(int, input().split())
t = toi(input())
s = [toi(input()) ^ t for _ in range(n)]
q = int(input())
qs = [tuple(map(int, input().split())) for _ in range(q)]

st = set(s)
tmp = s[:]
for i, j in qs:
    i -= 1
    tmp[i] ^= 1 << (k - j)
    st.add(tmp[i])
vals = sorted(st)
idx = {v: p for p, v in enumerate(vals)}
V = len(vals)
bit = [0] * (V + 1)


def add(p, x):
    p += 1
    while p <= V:
        bit[p] += x
        p += p & -p


def sm(p):
    p += 1
    r = 0
    while p > 0:
        r += bit[p]
        p -= p & -p
    return r


for v in s:
    add(idx[v], 1)

allone = (1 << k) - 1
out = []
for i, j in qs:
    i -= 1
    v = s[i]
    add(idx[v], -1)
    v ^= 1 << (k - j)
    s[i] = v
    add(idx[v], 1)
    if n == m:
        out.append("No" if v == allone else "Yes")
    else:
        out.append("Yes" if sm(idx[v]) <= m else "No")
print("\n".join(out))
