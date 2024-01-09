import copy
from collections import defaultdict
from collections import deque

N = int(input())
a = list(map(int, input().split()))


m = defaultdict(deque)

b = sorted(a)
for i in range(N) :
    m[b[i]].append(i+1)


ans = []
for i in range(N) :
    x = m[a[i]].popleft()
    ans.append(x)

print(*ans)