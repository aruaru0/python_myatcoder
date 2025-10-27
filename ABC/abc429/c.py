from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

m = defaultdict(int)

for x in a:
    m[x] += 1

ans = 0
for c in m:
    if m[c] >= 2:
        ans += m[c] * (m[c] - 1) // 2 * (N - m[c])

print(ans)


