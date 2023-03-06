# Contest ID: typical90
# Problem ID: typical90_am ( https://atcoder.jp/contests/typical90/tasks/typical90_am )
# Title: 039. Tree Distance（★5）
# Language: Python (3.8.2)
# Submitted: 2021-05-13 08:45:24 +0000 UTC ( https://atcoder.jp/contests/typical90/submissions/22554955 ) 

import sys
sys.setrecursionlimit(10**5+1000)

N = int(input())
node = [[] for _ in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node[a].append((b, i))
    node[b].append((a, i))

child = [0] * (N-1)


def dfs(cur, prev, enum, cnt):
    ret = 1
    for e in node[cur]:
        if e[0] == prev:
            continue
        ret += dfs(e[0], cur, e[1], cnt+1)

    if enum != -1:
        child[enum] = ret
    return ret


dfs(0, -1, -1, 0)

ans = 0
for i in range(N-1):
    ans += child[i]*(N-child[i])

print(ans)
