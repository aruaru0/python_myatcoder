class BIT:
    def __init__(self, n):
        self.n = n
        self.d = [0] * (n + 2)
    def add(self, i, x):
        i += 1
        n = self.n
        d = self.d
        while i <= n:
            d[i] += x
            i += i & -i
    def sum(self, i):
        s = 0
        d = self.d
        while i > 0:
            s += d[i]
            i -= i & -i
        return s

n, q = map(int, input().split())
c = list(map(int, input().split()))

b1 = BIT(n + 2)
b2 = BIT(n + 2)

for i, val in enumerate(c):
    b1.add(i, val)
    b1.add(i + 1, -val)
    b2.add(i, val * i)
    b2.add(i + 1, -val * (i + 1))

def r_add(l, r, v):
    b1.add(l, v)
    b1.add(r + 1, -v)
    b2.add(l, v * l)
    b2.add(r + 1, -v * (r + 1))

def p_sum(x):
    return b1.sum(x) * x - b2.sum(x)

def r_sum(l, r):
    return p_sum(r + 1) - p_sum(l)

for _ in range(q):
    t, *rest = map(int, input().split())
    if t == 1:
        l, r, v = rest
        r_add(l - 1, r - 1, v)
    else:
        l, r = rest
        print(r_sum(l - 1, r - 1))
