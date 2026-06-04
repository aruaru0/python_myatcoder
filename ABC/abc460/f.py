from atcoder.segtree import SegTree
import sys
input = sys.stdin.readline

class SparseTable:
    def __init__(self, a, op=max):
        f = a[:]
        self.st = [f]
        j, n = 1, len(f)
        while 2 * j <= n:
            f = [op(f[i], f[i+j]) for i in range(n - 2*j + 1)]
            self.st.append(f)
            j <<= 1
        self.op = op

    def query(self, l, r):
        j = (r-l+1).bit_length() - 1
        return self.op(self.st[j][l], self.st[j][r - (1<<j) + 1])

class LCA:
    def __init__(self, G, n):
        self.parent = [-1] * n
        self.depth = [0] * n
        self.visit_order = []
        self.first_appearance = [-1] * n

        stack = [0]
        while stack:
            i = stack.pop()
            self.first_appearance[i] = len(self.visit_order)
            self.visit_order.append(i)
            G[i] = [j for j in G[i] if j != self.parent[i]]
            for j in G[i]:
                self.parent[j] = i
                self.depth[j] = self.depth[i] + 1
                stack.append(j)

        self.st = SparseTable(self.visit_order, lambda i, j: j if self.depth[j] < self.depth[i] else i)

    def get_lca(self, x, y):
        if x == y:
            return x
        a, b = self.first_appearance[x], self.first_appearance[y]
        if a > b:
            a, b = b, a
        return self.parent[self.st.query(a+1, b)]

    def get_distance(self, x, y):
        lca_node = self.get_lca(x, y)
        return self.depth[x] + self.depth[y] - 2 * self.depth[lca_node]

def solve(n, u, v, q, queries):
    u = [_-1 for _ in u]
    v = [_-1 for _ in v]
    queries = [_-1 for _ in queries]
    G = [[] for i in range(n)]
    for i, j in zip(u, v):
        G[i].append(j)
        G[j].append(i)

    lca = LCA(G, n)
    def op(a, b):
        if a[0] == -1: return b
        if b[0] == -1: return a
        best_pair = a
        max_dist = lca.get_distance(a[0], a[1])
        candidates = list(a) + list(b)
        for i in range(3):
            for j in range(i+1, 4):
                x, y = candidates[i], candidates[j]
                d = lca.get_distance(x, y)
                if d > max_dist:
                    max_dist = d
                    best_pair = (x, y)
        return best_pair

    e = (-1, -1)
    initial_array =[(i, i) for i in range(n)]
    seg = SegTree(op, e, initial_array)
    is_black = [True] * n
    
    ans = []
    for x in queries:
        is_black[x] ^= True
        new_value = (x, x) if is_black[x] else (-1, -1)
        seg.set(x, new_value)
        i, j = seg.all_prod()
        ans.append(lca.get_distance(i, j))
    return ans

if __name__ == "__main__":
    n = int(input())
    u, v = [0]*(n-1), [0]*(n-1)
    for i in range(n-1):
        u[i], v[i] = map(int, input().split())
    q = int(input())
    queries = [int(input()) for i in range(q)]
    print(*solve(n, u, v, q, queries), sep="\n")


