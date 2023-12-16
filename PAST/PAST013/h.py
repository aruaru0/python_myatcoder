

class BIT :
    def __init__(self, n) :
        self.v = [0 for _ in range(n+1)]
    
    def sum(self, a) :
        ret = 0
        i = a+1
        while i > 0 :
            ret += self.v[i-1]
            i -= i & -i
        return ret
    
    def rangeSum(self, x, y) :
        if  y == 0 :
            return 0
        y -= 1
        if x == 0 :
            return self.sum(y)
        else:
            return self.sum(y) - self.sum(x-1)
        
    def add(self, a, w) :
        n = len(self.v)
        i = a+1
        while i <= n :
            self.v[i-1] += w
            i += i & -i
        

D = int(input())
n = [ord(n)-ord('0') for n in list(input())]

bit = [BIT(D+1) for _ in range(10)]

for i, e in enumerate(n) :
    for j in range(10):
        bit[j].add(i, abs(j-e))

# for i in range(10):
#     l = []
#     for j in range(D) :
#         l.append(bit[i].rangeSum(j, j+1))

#     print(l)

ans = 0
for i in range(D):
    v = n[i]
    ans += bit[v].rangeSum(i, D+1)

print(ans)