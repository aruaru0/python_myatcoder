MOD = 998244353

def solve():
    N = input().strip()
    L = len(N)

    # マスク圧縮: popcount≦3 の全ビットマスク + overflow
    masks = []
    idx_of = {}
    for m in range(1 << 10):
        pc = m.bit_count()
        if pc <= 3:
            idx_of[m] = len(masks)
            masks.append(m)
    OV = len(masks)
    Msz = OV + 1
    pc_of = [m.bit_count() for m in masks] + [4]

    # 遷移表
    nxt = [[0] * 10 for _ in range(Msz)]
    for mi, m in enumerate(masks):
        for d in range(10):
            nm = m | (1 << d)
            p = nm.bit_count()
            if p <= 3:
                nxt[mi][d] = idx_of[nm]
            else:
                nxt[mi][d] = OV
    for d in range(10):
        nxt[OV][d] = OV

    # dp[started][mask][mod3*2+has3]
    dp = [[[0] * 6 for _ in range(Msz)] for _ in range(2)]

    # tight=1
    t1_st = 0
    t1_mi = 0
    t1_m3 = 0
    t1_h3 = 0

    for i in range(L):
        D = int(N[i])
        ndp = [[[0] * 6 for _ in range(Msz)] for _ in range(2)]

        # tight=0 遷移
        for st in (0, 1):
            for mi in range(Msz):
                row = dp[st][mi]
                for d in range(10):
                    if st == 0 and d == 0:
                        nst = 0
                        nmi = 0
                        nd3 = 0
                        nd_h3 = 0
                    elif st == 0:
                        nst = 1
                        nmi = idx_of[1 << d]
                        nd3 = d % 3
                        nd_h3 = 1 if d == 3 else 0
                    else:
                        nst = 1
                        nmi = nxt[mi][d]
                        nd3 = d % 3
                        nd_h3 = 1 if d == 3 else 0
                    for h3 in (0, 1):
                        for m3 in range(3):
                            cnt = row[m3 * 2 + h3]
                            if cnt == 0:
                                continue
                            nm3 = (m3 + nd3) % 3
                            nh3 = h3 | nd_h3
                            ndp[nst][nmi][nm3 * 2 + nh3] = (
                                ndp[nst][nmi][nm3 * 2 + nh3] + cnt
                            ) % MOD

        # tight=1 遷移
        if t1_st == 0:
            for d in range(D):
                if d == 0:
                    ndp[0][0][0] = (ndp[0][0][0] + 1) % MOD
                else:
                    nmi = idx_of[1 << d]
                    nd3 = d % 3
                    nh3 = 1 if d == 3 else 0
                    ndp[1][nmi][nd3 * 2 + nh3] = (ndp[1][nmi][nd3 * 2 + nh3] + 1) % MOD
            if D == 0:
                t1_st = 0
                t1_mi = 0
                t1_m3 = 0
                t1_h3 = 0
            else:
                t1_st = 1
                t1_mi = idx_of[1 << D]
                t1_m3 = D % 3
                t1_h3 = 1 if D == 3 else 0
        else:
            for d in range(D):
                nmi = nxt[t1_mi][d]
                nd3 = d % 3
                nh3 = 1 if d == 3 else 0
                nm3 = (t1_m3 + nd3) % 3
                nh3_f = t1_h3 | nh3
                ndp[1][nmi][nm3 * 2 + nh3_f] = (ndp[1][nmi][nm3 * 2 + nh3_f] + 1) % MOD
            nmi = nxt[t1_mi][D]
            nd3 = D % 3
            nh3 = 1 if D == 3 else 0
            t1_mi = nmi
            t1_m3 = (t1_m3 + nd3) % 3
            t1_h3 = t1_h3 | nh3

        dp = ndp

    def contrib(cnt, pc, mod3, has3):
        if cnt == 0:
            return 0
        a = 1 if mod3 == 0 else 0
        b = 1 if has3 else 0
        c = 1 if pc == 3 else 0
        return cnt if a + b + c == 1 else 0

    ans = 0
    # started=0 は数 0 を表すので除外
    for mi in range(Msz):
        row = dp[1][mi]
        pc = pc_of[mi]
        for h3 in (0, 1):
            for m3 in range(3):
                cnt = row[m3 * 2 + h3]
                ans = (ans + contrib(cnt, pc, m3, h3)) % MOD
    # tight=1 (N 自身)
    ans = (ans + contrib(1, pc_of[t1_mi], t1_m3, t1_h3)) % MOD

    print(ans)


solve()
