class BIT :
    def __init__(self, n) :
        self.size = n
        self.bit = [0] * (n + 1)

    def add(self, i, x) :
        i += 1
        while i <= self.size :
            self.bit[i] += x
            i += i & -i

    def sum(self, i) :
        i += 1
        s = 0
        while i > 0 :
            s += self.bit[i]
            i -= i & -i
        return s
    
    def range_sum(self, l, r) :
        return self.sum(r-1) - self.sum(l-1)
    

n, q = map(int, input().split())
a = list(map(int, input().split()))

bit = BIT(n+1)

for i in range(n) :
    bit.add(i, a[i])


for _ in range(q) :
    s = list(map(int, input().split()))
    if s[0] == 1 :
        x = s[1] - 1
        bit.add(x, -a[x])
        bit.add(x+1, -a[x+1])
        a[x], a[x+1] = a[x+1], a[x]
        bit.add(x, a[x])
        bit.add(x+1, a[x+1])
    else :
        l, r = s[1]-1, s[2]
        print(bit.range_sum(l, r))
    # for i in range(n) :
    #     print(bit.range_sum(i, i), end=" ")
    # print()