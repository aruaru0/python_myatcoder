import sys, math

it = iter(sys.stdin.read().split())
t = int(next(it))
pow10 = [1]
for _ in range(10):
    pow10.append(pow10[-1] * 10)

out = []
for _ in range(t):
    c = int(next(it))
    d = int(next(it))

    ans = 0
    for l in range(1, 11): 
        low = max(c + 1, pow10[l - 1])
        high = min(c + d, pow10[l] - 1)
        if low > high:
            continue

        a = c * pow10[l] + low
        b = c * pow10[l] + high

        lo = math.isqrt(a)
        if lo * lo < a:
            lo += 1 
        hi = math.isqrt(b) 

        if hi >= lo:
            ans += hi - lo + 1

    print(ans)


