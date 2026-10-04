from itertools import combinations

n, v = map(int, input().split())
w = list(map(int, input().split()))

a = [i for i in range(n)]
ans = 0
for [x, y, z] in combinations(a, 3):
    if x+y+z+3 <= v :
        ans = max(ans, w[x]+w[y]+w[z])
print(ans)