from atcoder import dsu

n = int(input())
a = list(map(int, input().split()))

max_a = max(a)

pos = [-1] * (max_a+1)
for i, v in enumerate(a) :
    pos[v] = i

uf = dsu.DSU(n)
ans = 0

for x in range(max_a, 0, -1) :
    first = -1
    for y in range(x, max_a+1, x) :
        if pos[y] != -1 :
            if first == -1 : 
                first = pos[y]
            else : 
                if uf.same(first, pos[y]) == False :
                    uf.merge(first, pos[y])
                    ans += x
print(ans)