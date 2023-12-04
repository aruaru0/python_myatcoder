from collections import defaultdict
N = int(input())
a = list(map(int, input().split()))

d = defaultdict(list)
for i, e in enumerate(a):
    d[e].append(i)


a = sorted(list(d))[::-1]

ans = [0] * N
tot = 0
for e in a :
    # print(d[e])
    for v in d[e] :
        # print(v)
        ans[v] = tot
    tot += len(d[e]) * e

print(*ans)