
class BIT :
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.tree[i-1] += x
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i-1]
            i -= i & -i
        return s

    def query_range(self, l, r):
        return self.query(r) - self.query(l)

N, Q = map(int, input().split())
s = list(map(int, input().split()))

bit = BIT(N)
for i in range(N):
    bit.add(i, s[i])

for _ in range(Q):
    t = list(map(int, input().split()))
    if t[0] == 1:
        l, r = t[1]-1, t[2]
        print(bit.query_range(l, r))
    else:
        x, v = t[1] - 1, t[2]
        bit.add(x, v - s[x])
        s[x] = v