H, W, Q = map(int, input().split())
q = []
for _ in range(Q):
    R, C, X = input().split()
    q.append((int(R) - 1, int(C) - 1, X))

filled = [0] * H
ans = [['A'] * W for _ in range(H)]

for R, C, X in reversed(q):
    lo, hi = 0, R
    r0 = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if filled[mid] < C + 1:
            r0 = mid
            hi = mid - 1
        else:
            lo = mid + 1
    if r0 == -1:
        continue
    for r in range(r0, R + 1):
        if filled[r] >= C + 1:
            break
        for c in range(filled[r], C + 1):
            ans[r][c] = X
        filled[r] = C + 1

for row in ans:
    print(''.join(row))
