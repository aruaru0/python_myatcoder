import sys
it = iter(sys.stdin.read().split())
t = int(next(it))
m = int(next(it))

cases = []
max_l = 0
for _ in range(t):
    n = int(next(it))
    c = [int(next(it)) for __ in range(n)]
    l = sum(c)
    cases.append((l, c))
    if l > max_l:
        max_l = l

# ---------- 前計算 ----------
MAX = max_l
spf = list(range(MAX + 1))
for i in range(2, int(MAX ** 0.5) + 1):
    if spf[i] == i:
        step = i
        start = i * i
        for j in range(start, MAX + 1, step):
            if spf[j] == j:
                spf[j] = i

primes = []
idx_of = {}
for x in range(2, MAX + 1):
    if spf[x] == x:
        idx_of[x] = len(primes)
        primes.append(x)
P = len(primes)

# exp[n][j] : exponent of primes[j] in n!
exp = [[0] * P for _ in range(MAX + 1)]
for n in range(2, MAX + 1):
    prev = exp[n - 1]
    cur = exp[n]
    cur[:] = prev[:]
    x = n
    while x > 1:
        p = spf[x]
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        j = idx_of[p]
        cur[j] += cnt

out_lines = []
for l, c in cases:
    vec = exp[l][:]          # copy
    for ci in c:
        row = exp[ci]
        for j in range(P):
            vec[j] -= row[j]

    ans = 1 % m
    for j, e in enumerate(vec):
        if e:
            ans = (ans * pow(primes[j], e, m)) % m
    out_lines.append(str(ans))

sys.stdout.write("\n".join(out_lines))
