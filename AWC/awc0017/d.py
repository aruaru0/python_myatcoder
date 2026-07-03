from collections import defaultdict
from itertools import combinations


n, m, k = map(int, input().split())

a = list(map(int, input().split()))


pair = defaultdict(int)
for _ in range(m) :
    u, v, b = map(int, input().split())
    u-=1
    v-=1
    pair[(u, v)] = b


p = [i for i in range(n)]

ans = -10**18
for sel in combinations(p, k) :
    plus = sum(a[i] for i in sel)
    minus = 0
    for u in sel:
        for v in sel:
            minus += pair[(u, v)]
    
    ans = max(ans, plus-minus)

print(ans)


