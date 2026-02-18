def mul(A, B):
    n = len(A)
    INF = 10 ** 19
    R = [[INF] * n for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        Ri = R[i]
        for k in range(n):
            aik = Ai[k]
            if aik == INF:
                continue
            Bk = B[k]
            s = aik
            for j in range(n):
                v = s + Bk[j]
                if v < Ri[j]:
                    Ri[j] = v
    return R


def mpow(M, e):
    n = len(M)
    INF = 10 ** 19
    I = [[INF] * n for _ in range(n)]
    for i in range(n):
        I[i][i] = 0
    res = I
    base = M
    while e:
        if e & 1:
            res = mul(res, base)
        base = mul(base, base)
        e >>= 1
    return res


N, K = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(N)]
ans = mpow(C, K)
for i in range(N):
    print(ans[i][i])


