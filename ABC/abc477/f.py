import sys

input = sys.stdin.readline


# 関数スコープにしてループ内の変数参照を高速化する
def solve():
    n, m, q = map(int, input().split())
    L = [0]*(n+1)
    R = [0]*(n+1)
    for i in range(1, n+1):
        L[i], R[i] = map(int, input().split())

    # 行方向的累積 G(x,t) = 行1..x・列1..t の黒マス数 を求める。
    # 行 x を追加すると列 cnt(j) が区間 [L_x,R_x] だけ +1 される。
    # 差分 d[j] = cnt(j)-cnt(j-1) にすると L_x で +1, R_x+1 で -1 の点更新。
    # G(x,t) = (t+1)*P(t) - S(t),  P(t)=Σ_{j<=t}d[j], S(t)=Σ_{j<=t}j*d[j]
    # cnt(t) は 0<=cnt(t)<=n<2^18 なので P と S を 1 本の Fenwick Tree に
    # まとめる: 値 = S*2^19 + P  （下位 19bit が P）
    SH = 19
    MSK = (1 << SH) - 1

    # クエリ k は 行 b のイベント(+1) と 行 a-1 のイベント(-1) に分割
    ev = [None]*(n+1)
    for k in range(q):
        a, b, c, d = map(int, input().split())
        e = ev[b]
        if e is None:
            ev[b] = [(d, c-1, k)]
        else:
            e.append((d, c-1, k))
        e = ev[a-1]
        if e is None:
            ev[a-1] = [(d, c-1, ~k)]
        else:
            e.append((d, c-1, ~k))

    bit = [0]*(m+1)
    ans = [0]*q
    for x in range(1, n+1):
        p = L[x]
        u = (p << SH) + 1
        while p <= m:
            bit[p] += u
            p += p & -p
        p = R[x]+1
        if p <= m:
            u = (p << SH) + 1
            while p <= m:
                bit[p] -= u
                p += p & -p
        e = ev[x]
        if e is None:
            continue
        for t1, t2, k in e:
            v = 0
            p = t1
            while p:
                v += bit[p]
                p &= p-1
            r = (t1+1)*(v & MSK) - (v >> SH)
            v = 0
            p = t2
            while p:
                v += bit[p]
                p &= p-1
            r -= (t2+1)*(v & MSK) - (v >> SH)
            if k >= 0:
                ans[k] += r
            else:
                ans[~k] -= r

    print('\n'.join(map(str, ans)))


solve()
