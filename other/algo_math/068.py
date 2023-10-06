N, K = map(int, input().split())
v = list(map(int, input().split()))


def gcd(a, b) :
    if b == 0 : return a
    return gcd(b, a%b)

def lcm(a, b) :
    return a//gcd(a,b)*b

def calc(v, n) :
    # print(v, n)
    l = 1
    for e in v:
        l = lcm(l, e)

    ret = n // l
    if len(v)%2 :
        return -ret
    return ret

bit = 1<<K
tot = 0
for b in range(1,bit) :
    sel = []
    for i in range(K):
        if (b>>i) % 2 :
            sel.append(v[i])
    tot -= calc(sel, N)

print(tot)