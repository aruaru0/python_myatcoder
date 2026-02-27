from collections import defaultdict

N, S = map(int,input().split())
a = list(map(int, input().split()))

def f(x) :
    ret = defaultdict(int)
    n = len(x)
    for s in range(1<<n) : 
        tot = 0
        for j in range(n) :
            if (s>>j)%2 :
                tot += x[j]
        ret[tot] += 1

    return ret


m = N//2
x = f(a[:m])
y = f(a[m:])

ans = 0
for e in x:
    d = S - e
    ans += x[e] * y[d]

print(ans)