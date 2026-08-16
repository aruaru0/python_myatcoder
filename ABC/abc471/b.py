from collections import defaultdict

n = int(input())
s = [input() for _ in range(n)]
mp = defaultdict(int)
for e in s:
    mp[e.lower()] += 1


print(max(mp.values()))