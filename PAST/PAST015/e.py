from itertools import combinations

n, k = map(int, input().split())

a = list(map(int, input().split()))

tot = 0
for e in combinations([i for i in range(n)], k) :
    for i in e:
        tot += a[i]

print(tot)

