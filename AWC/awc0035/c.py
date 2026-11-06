from collections import deque

n, m = map(int, input().split())
t = list(map(int, input().split()))


w = [0] * n
node = [[] for _ in range(n)]
for _ in range(m) :
    u, v = map(int, input().split())
    u-=1
    v-=1
    node[u].append(v)
    w[v] += 1

q = deque()
ans = []
for i in range(n) :
    if w[i] > t[i] :
        q.append(i)
        ans.append(i+1)

while q :
    cur = q.popleft()
    for e in node[cur] :
        if w[e] <= t[e] :
            w[e] += 1
            if w[e] > t[e] :
                q.append(e)
                ans.append(e+1)

if len(ans) == 0 : 
    print(-1)
else:
    print(*sorted(ans))