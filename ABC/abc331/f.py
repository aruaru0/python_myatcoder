# --- セグメント木 -----
class segtree():
    n=1
    size=1
    log=2
    d=[0]
    op=None
    e=10**15
    def __init__(self,V,OP,E):
        self.n=len(V)
        self.op=OP
        self.e=E
        self.log=(self.n-1).bit_length()
        self.size=1<<self.log
        self.d=[E for i in range(2*self.size)]
        for i in range(self.n):
            self.d[self.size+i]=V[i]
        for i in range(self.size-1,0,-1):
            self.update(i)
    def set(self,p,x):
        assert 0<=p and p<self.n
        p+=self.size
        self.d[p]=x
        for i in range(1,self.log+1):
            self.update(p>>i)
    def get(self,p):
        assert 0<=p and p<self.n
        return self.d[p+self.size]
    def prod(self,l,r):
        assert 0<=l and l<=r and r<=self.n
        sml=self.e
        smr=self.e
        l+=self.size
        r+=self.size
        while(l<r):
            if (l&1):
                sml=self.op(sml,self.d[l])
                l+=1
            if (r&1):
                smr=self.op(self.d[r-1],smr)
                r-=1
            l>>=1
            r>>=1
        return self.op(sml,smr)
    def all_prod(self):
        return self.d[1]
    def max_right(self,l,f):
        assert 0<=l and l<=self.n
        assert f(self.e)
        if l==self.n:
            return self.n
        l+=self.size
        sm=self.e
        while(1):
            while(l%2==0):
                l>>=1
            if not(f(self.op(sm,self.d[l]))):
                while(l<self.size):
                    l=2*l
                    if f(self.op(sm,self.d[l])):
                        sm=self.op(sm,self.d[l])
                        l+=1
                return l-self.size
            sm=self.op(sm,self.d[l])
            l+=1
            if (l&-l)==l:
                break
        return self.n
    def min_left(self,r,f):
        assert 0<=r and r<=self.n
        assert f(self.e)
        if r==0:
            return 0
        r+=self.size
        sm=self.e
        while(1):
            r-=1
            while(r>1 and (r%2)):
                r>>=1
            if not(f(self.op(self.d[r],sm))):
                while(r<self.size):
                    r=(2*r+1)
                    if f(self.op(self.d[r],sm)):
                        sm=self.op(self.d[r],sm)
                        r-=1
                return r+1-self.size
            sm=self.op(self.d[r],sm)
            if (r& -r)==r:
                break
        return 0
    def update(self,k):
        self.d[k]=self.op(self.d[2*k],self.d[2*k+1])
    def __str__(self):
        return str([self.get(i) for i in range(self.n)])
    

# ----- ここからメインプログラム　--------
N, Q = map(int, input().split())

# 文字列Sと逆順のTを作成。同時に整数値に変換
s = [ord(c) for c in list(input())]
t = s[::-1]

# 素数
p = 998244353

# xをランダムに生成
import random
x = random.randint(10000, p) % p

# セグメント木にのせるデータに変換
s = [[e, x, p] for e in s]
t = [[e, x, p] for e in t]

# funcの定義
def op(x, y) :
    h0, x0, p = x
    h1, x1, p = y
    return [(h0 + h1 * x0)%p, (x0*x1)%p, p]

# セグメント木の生成
segS = segtree(s, op, [0,1,p])
segT = segtree(t, op, [0,1,p])

# ループ
for _ in range(Q) :
    v = input().split()
    if v[0] == '1' :
        pos, c = int(v[1])-1, ord(v[2])
        segS.set(pos, [c, x, p])
        segT.set(N-1-pos, [c, x, p])
    else :
        l, r = int(v[1])-1, int(v[2])
        h0 = segS.prod(l, r)[0]
        h1 = segT.prod(N-r, N-l)[0]
        if h0 == h1 :
            print("Yes")
        else:
            print("No")
