import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
d = defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    d[(a, b)] += 1
INF = 5 * 10**5 + 1

ans = [0] + [n] * (INF - 1)
for (a, b), v in d.items():
    ans[0] += a * v
    for k in range(b - a, INF, b):
        ans[k] -= b * v

for i in range(1, INF):
    ans[i] += ans[i - 1]
for _ in range(int(input())):
    print(ans[int(input())])
