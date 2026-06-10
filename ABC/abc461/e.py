class BIT:
    def __init__(self, n):
        self.n = n
        self.d = [0] * (n + 1)
    def add(self, i, x):
        i += 1
        n = self.n
        while i <= n:
            self.d[i] += x
            i += i & -i
    def sum(self, i):
        if i < 0:
            return 0
        if i >= self.n:
            i = self.n - 1
        i += 1
        s = 0
        while i > 0:
            s += self.d[i]
            i -= i & -i
        return s

n, q = map(int, input().split())
m = q + 1
bc = BIT(m)
br = BIT(m)
bc.add(0, n)
br.add(0, n)
rb = [0] * n
cw = [0] * n
tt = 0
out = []

for i in range(1, q + 1):
    T, *p = map(int, input().split())
    if T == 1:
        r = p[0] - 1
        od = rb[r]
        nd = i
        d = bc.sum(nd - 1) - bc.sum(od - 1)
        tt += d
        br.add(od, -1)
        br.add(nd, 1)
        rb[r] = nd
    else:
        c = p[0] - 1
        od = cw[c]
        nd = i
        cnt = br.sum(nd) - br.sum(od)
        tt -= cnt
        bc.add(od, -1)
        bc.add(nd, 1)
        cw[c] = nd
    out.append(str(tt))

print('\n'.join(out))
