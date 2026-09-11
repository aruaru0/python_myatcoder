N = int(input())
A = list(map(int, input().split()))

D = [0] * (N + 1)
for i in range(1, N + 1):
    D[i] = A[i - 1] - A[0]

mu = [0] * (N + 1)
mu[1] = 1
is_comp = bytearray(N + 1)
primes = []
for i in range(2, N + 1):
    if not is_comp[i]:
        primes.append(i)
        mu[i] = -1
    for p in primes:
        v = i * p
        if v > N:
            break
        is_comp[v] = 1
        if i % p == 0:
            mu[v] = 0
            break
        mu[v] = -mu[i]

pre = [0] * (N + 1)
for i in range(1, N + 1):
    pre[i] = pre[i - 1] + mu[i]

B = [0] * (N + 1)
for i in range(1, N + 1):
    s = 0
    k = i
    d = 1
    while k <= N:
        m = mu[d]
        if m:
            s += m * D[k]
        k += i
        d += 1
    B[i] = s

lo = 0
mx = 0
for i in range(1, N + 1):
    if D[i] > mx:
        mx = D[i]
if mx > lo:
    lo = mx
hi = 10 ** 30
ok = True
for i in range(1, N + 1):
    M = pre[N // i]
    b = B[i]
    if M > 0:
        need = -((-b) // M)
        if need > lo:
            lo = need
    elif M < 0:
        cap = b // M
        if cap < hi:
            hi = cap
    else:
        if b > 0:
            ok = False
            break

if ok and lo <= hi:
    print(lo)
else:
    print(-1)
