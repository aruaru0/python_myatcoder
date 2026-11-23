from itertools import groupby

n = int(input())
c = list(map(int, input().split()))

lengths = [len(list(g)) for _, g in groupby(c)]

ans = []
m = len(lengths)
for idx, length in enumerate(lengths):
    for k in range(1, length + 1):
        d = 10**9
        if idx > 0:
            d = min(d, k)  # 左の境界までの距離
        if idx + 1 < m:
            d = min(d, length + 1 - k)  # 右の境界までの距離
        ans.append(d)

print(*ans)
