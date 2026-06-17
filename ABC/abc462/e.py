T = int(input())
for _ in range(T):
    A, B, X, Y = map(int, input().split())
    if A < B:
        A, B = B, A
        X, Y = Y, X
    h = abs(X)
    v = abs(Y)
    N = h + v
    if N == 0:
        print(0)
        continue
    odd = (N + 1) // 2
    ex = v - odd
    if ex < 0:
        ex = -ex
    if A > 3 * B:
        print(B * (N + 2 * ex))
    else:
        print(B * N + ex * (A - B))
