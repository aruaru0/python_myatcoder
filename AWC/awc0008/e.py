class BIT :
    def __init__(self, n):
        self.n = n
        self.v = [0] * n
    
    def add(self, a, w):
        i = a+1
        while i <= self.n:
            self.v[i-1] += w
            i += i&-i
    
    def sum(self, a):
        ret = 0
        i = a+1
        while i > 0:
            ret += self.v[i-1]
            i -= i&-i
        return ret
    
    def rangeSum(self, x, y):
        if  y == 0 :
            return 0
        y -= 1
        if x == 0 :
            return self.sum(y)
        else :
            return self.sum(y) - self.sum(x-1)


n = int(input())
a = list(map(int, input().split()))

bit = BIT(n+1)

cnt = 0
for i in range(n):
    cnt += bit.rangeSum(a[i], n+1)
    bit.add(a[i], 1)
    

print(cnt)