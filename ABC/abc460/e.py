import math

MOD = 998244353
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    ans = 0
    d = 1
    while True:
        L = 10 ** (d - 1)
        if L > N:
            break
        U = min(N, 10 ** d - 1)
        cnt_y = U - L + 1

        r = pow(10, d, M)
        g = math.gcd((r - 1) % M, M)
        step = M // g
        cnt_x = N // step

        ans = (ans + cnt_x * cnt_y) % MOD
        d += 1

    print(ans)