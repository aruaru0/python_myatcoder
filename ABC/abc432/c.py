N, X, Y = map(int, input().split())
a = list(map(int, input().split()))

D = Y - X                     # 重さの差
r = (X * a[0]) % D            # 余りは全員で同じはず

lo = 0                        # max t_i
hi = None                     # min(t_i + A_i)
s = 0                         # Σ t_i

for v in a:
    if (X * v) % D != r:      # 余りが揃わない → 不可能
        print(-1)
        exit()

    t = (X * v - r) // D
    s += t
    if t > lo:
        lo = t
    h = t + v
    if hi is None or h < hi:
        hi = h

if lo > hi: 
    print(-1)
    exit()

C = hi
ans = N * C - s
print(ans)

