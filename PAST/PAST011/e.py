n = int(input())


def f(m) :
    return (1+2*m-1)*m // 2

ok, ng = 0, 10**18
while ok+1 != ng :
    m = (ok+ng)//2
    if f(m) >= n :
        ng = m
    else :
        ok = m

diff = n - f(ok)

def calc(start, n) :
    if n <= start : return start - n + 1
    return 1 + (n - start)


print(calc(ok+1, diff))

