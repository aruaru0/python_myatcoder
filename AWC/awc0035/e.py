from collections import deque

n = int(input())
h = list(map(int, input().split()))

cnt = 0
q = deque()
for i in range(n) :
    while len(q)!=0 and q[-1] <= h[i] :
        q.pop()
    cnt += len(q)
    q.append(h[i])

print(cnt)
    