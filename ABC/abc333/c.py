from itertools import combinations

N = int(input())

n = []
x = 1
for i in range(36) :
    n.append(x)
    if i%3 == 2: 
        x = x * 10 + 1

a = set()
for v in combinations(n, 3) :
    tot = 0
    for e in v : tot += e
    a.add(tot)

a = sorted(list(a))

print(a[N-1])


