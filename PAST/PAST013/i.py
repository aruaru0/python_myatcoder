from collections import deque

N, M = map(int, input().split())

node = [[] for _ in range(N)]
cnt = [0 for _ in range(N)]
for _ in range(M) :
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node[a].append(b)
    cnt[b] += 1


q = deque()
for i in range(N) :
    if cnt[i] == 0 :
        q.append(i)


used = [False for _ in range (N)]
while len(q) != 0 :
    cur = q.popleft()
    used[cur] = True
    for e in node[cur]:
        cnt[e] -= 1
        if cnt[e] == 0 :
            q.append(e)
    
ok = True
for i in range(N) :
    if used[i] == False :
        ok = False

if ok :
    print("Yes")
else:
    print("No")
