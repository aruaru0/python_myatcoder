import sys

def solve() -> None:
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # C_i = (B_i - A_i - A_{i+1}) % M
    C = [(B[i] - A[i] - A[i + 1]) % M for i in range(N - 1)]

    # Compute d_i and e_i
    # e[i] = (-1)^{i-1}, i.e. e[0] = 1, e[1] = -1, e[2] = 1, ...
    d = [0] * N
    e = [1] * N
    for i in range(1, N):
        e[i] = -e[i - 1]
        d[i] = (C[i - 1] - d[i - 1]) % M

    base = sum(d)
    pos = sum(1 for v in e if v == 1)
    neg = N - pos
    slope = pos - neg

    # Build events: (position, delta_cnt_pos, delta_cnt_neg)
    events = {}
    for i in range(N):
        if e[i] == 1:
            bp = M - d[i]
            if 1 <= bp < M:
                events[bp] = events.get(bp, [0, 0])
                events[bp][0] += 1
        else:  # e[i] == -1
            bp = d[i] + 1
            if bp < M:
                events[bp] = events.get(bp, [0, 0])
                events[bp][1] += 1

    # Sweep
    ans = base  # f(0)
    cnt_pos = 0
    cnt_neg = 0
    prev_t = 0
    f_prev = base

    for t in sorted(events.keys()):
        dp, dn = events[t]

        # Interval [prev_t, t-1]
        if t - 1 > prev_t and slope < 0:
            val = f_prev + slope * (t - 1 - prev_t)
            if val < ans:
                ans = val

        # Apply changes at t
        cnt_pos += dp
        cnt_neg += dn

        # f(t)
        f_t = base + t * slope - M * cnt_pos + M * cnt_neg
        if f_t < ans:
            ans = f_t

        f_prev = f_t
        prev_t = t

    # Last interval [prev_t, M-1]
    if M - 1 > prev_t and slope < 0:
        val = f_prev + slope * (M - 1 - prev_t)
        if val < ans:
            ans = val

    print(ans)


solve()
