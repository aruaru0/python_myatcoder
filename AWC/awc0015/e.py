class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)

    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += i & (-i)

    def query(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & (-i)
        return s

N, Q = map(int, input().split())
P = list(map(int, input().split()))
qs = []
for i in range(Q):
    L, R = map(int, input().split())
    qs.append((L, R, i))

qs.sort(key=lambda x: x[1])

bit = BIT(N)
lp = [0] * (N + 1)
ans = [0] * Q
qi = 0

for i in range(1, N + 1):
    val = P[i-1]
    if lp[val]:
        bit.add(lp[val], -1)
    bit.add(i, 1)
    lp[val] = i
    
    while qi < Q and qs[qi][1] == i:
        L, R, k = qs[qi]
        ans[k] = bit.query(R) - bit.query(L - 1)
        qi += 1
        
print('\n'.join(map(str, ans)))
