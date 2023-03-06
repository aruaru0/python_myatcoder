# Contest ID: typical90
# Problem ID: typical90_aw ( https://atcoder.jp/contests/typical90/tasks/typical90_aw )
# Title: 049. Flip Digits 2（★6）
# Language: Python (3.8.2)
# Submitted: 2021-05-27 00:00:50 +0000 UTC ( https://atcoder.jp/contests/typical90/submissions/22939497 ) 

# union Find
class unionFind:
    def __init__(self, n):
        self.N = n
        self.u = [-1]*n

    def root(self, a):
        r = self.u[a]
        if r < 0:
            return a
        self.u[a] = self.root(r)
        return self.u[a]

    def unite(self, a, b):
        x = self.root(a)
        y = self.root(b)
        if x == y:
            return
        self.u[x] += self.u[y]
        self.u[y] = x

    def same(self, a, b):
        x = self.root(a)
        y = self.root(b)
        if x == y:
            return True
        return False

    def size(self, a):
        r = self.root(a)
        return -self.u[r]


N, M = map(int, input().split())

p = [list(map(int, input().split())) for _ in range(M)]

p.sort()

uf = unionFind(N+1)
cost = 0
for i in range(M):
    if uf.same(p[i][1]-1, p[i][2]):  # 同じグループに属している場合
        continue
    uf.unite(p[i][1]-1, p[i][2])
    #print(p[i][1]-1, p[i][2])
    cost += p[i][0]

#print(uf.u, uf.size(0), N)

if uf.size(0)-1 != N:
    print(-1)
else:
    print(cost)
