from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

tot = sum(A)
cnt = Counter(A)
vals = [v * c for v, c in cnt.items()]
vals.sort(reverse=True)
red = sum(vals[:K])
print(tot - red)
