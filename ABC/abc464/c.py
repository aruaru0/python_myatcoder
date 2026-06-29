n, m = map(int, input().split())
A = [0] * n
D = [0] * n
B = [0] * n
chg = [[] for _ in range(m + 2)]
for i in range(n):
    a, d, b = map(int, input().split())
    A[i] = a - 1
    D[i] = d
    B[i] = b - 1
    chg[d].append(i)

cnt = [0] * n
dist = 0

for i in range(n):
    col = B[i] if D[i] == 1 else A[i]
    if cnt[col] == 0:
        dist += 1
    cnt[col] += 1

for j in range(1, m + 1):
    print(dist)
    if j + 1 <= m:
        for i in chg[j + 1]:
            old = A[i]
            new = B[i]
            cnt[old] -= 1
            if cnt[old] == 0:
                dist -= 1
            if cnt[new] == 0:
                dist += 1
            cnt[new] += 1
