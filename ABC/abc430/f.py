T = int(input())
for _ in range(T):
    n = int(input())
    s = input().strip()
    m = n - 1                     # length of S

    # prefix lengths
    pr = [0] * m                  # consecutive 'R' ending at i
    pl = [0] * m                  # consecutive 'L' ending at i
    for i in range(m):
        if s[i] == 'R':
            pr[i] = (pr[i - 1] if i > 0 else 0) + 1
        else:
            pr[i] = 0
        if s[i] == 'L':
            pl[i] = (pl[i - 1] if i > 0 else 0) + 1
        else:
            pl[i] = 0

    # suffix lengths
    sr = [0] * m                  # consecutive 'R' starting at i
    sl = [0] * m                  # consecutive 'L' starting at i
    for i in range(m - 1, -1, -1):
        if s[i] == 'R':
            sr[i] = (sr[i + 1] if i + 1 < m else 0) + 1
        else:
            sr[i] = 0
        if s[i] == 'L':
            sl[i] = (sl[i + 1] if i + 1 < m else 0) + 1
        else:
            sl[i] = 0

    # difference array for the answer
    diff = [0] * (n + 3)          # 1‑based, need hi+1 ≤ n+1

    for v in range(n):           # vertex number v (0‑based)
        lr = pr[v - 1] if v > 0 else 0      # left side 'R'
        rl = sl[v]     if v < m else 0      # right side 'L'
        anc = lr + rl

        ll = pl[v - 1] if v > 0 else 0      # left side 'L'
        rr = sr[v]     if v < m else 0      # right side 'R'
        desc = ll + rr

        lo = anc + 1
        hi = n - desc

        diff[lo] += 1
        diff[hi + 1] -= 1

    cur = 0
    out = []
    for pos in range(1, n + 1):
        cur += diff[pos]
        out.append(str(cur))
    print(' '.join(out))


