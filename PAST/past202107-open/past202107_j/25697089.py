# Contest ID: past202107-open
# Problem ID: past202107_j ( https://atcoder.jp/contests/past202107-open/tasks/past202107_j )
# Title: J. Never Ending Journey
# Language: Python (3.8.2)
# Submitted: 2021-09-08 23:25:59 +0000 UTC ( https://atcoder.jp/contests/past202107-open/submissions/25697089 ) 

from collections import deque

N, M = map(int, input().split())

node = [[] for _ in range(N)]
cnt = [0 for _ in range(N)]

for i in range(M) :
    u, v = map(int, input().split())
    u-=1
    v-=1
    node[u].append(v)
    cnt[v]+=1

q = deque()
for i in range(N):
    if cnt[i] == 0 :
        q.append(i)

res = []
while len(q) != 0 :
    cur = q.pop()
    res.append(cur)
    for e in node[cur]:
        cnt[e]-=1
        if cnt[e] == 0 :
            q.append(e)


if len(res) == N :
    print("No")
else :
    print("Yes")
