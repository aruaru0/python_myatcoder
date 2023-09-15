
def matmul(A, B, mod):
    N = len(A)
    K = len(A[0])
    M = len(B[0])

    c = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N) :
        for j in range(K) :
            for k in range(M) :
                c[i][k] += A[i][j] * B[j][k] 
                c[i][k] %= mod
    return c

def pow_matrix(A, p, mod):
    n = len(A)
    c = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
    while p > 0 :
        if p%2 == 1 :
            c = matmul(c, A, mod)
        A = matmul(A, A, mod)
        p //= 2
    return c



n = int(input())

mod = 10**9
a = [[1,1],[1,0]]
ret = pow_matrix(a, n-2, mod)
ans = (ret[0][0] + ret[0][1]) % mod
print(ans)

