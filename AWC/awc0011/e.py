N, M = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b

# pref[i][w]: 先頭i個のアイテム(0..i-1)で容量w以下の最大価値
pref = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(N):
    a, b = A[i], B[i]
    pi = pref[i]
    pn = pref[i + 1]
    for w in range(M + 1):
        pn[w] = pi[w]
    for w in range(a, M + 1):
        val = pi[w - a] + b
        if val > pn[w]:
            pn[w] = val

# suff[i][w]: i番目以降(N-1..i)のアイテムで容量w以下の最大価値
suff = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(N - 1, -1, -1):
    a, b = A[i], B[i]
    si = suff[i]
    sn = suff[i + 1]
    for w in range(M + 1):
        si[w] = sn[w]
    for w in range(a, M + 1):
        val = sn[w - a] + b
        if val > si[w]:
            si[w] = val

opt = pref[N][M]

for i in range(N):
    a, b = A[i], B[i]
    pi = pref[i]
    si = suff[i + 1]
    best = 0
    left_max = M - a
    for w in range(left_max + 1):
        val = pi[w] + b + si[left_max - w]
        if val > best:
            best = val
    print("Yes" if best == opt else "No")
