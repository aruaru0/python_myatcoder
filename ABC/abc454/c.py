import sys

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

node = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a-=1
    b-=1
    node[a].append(b)


visited = [False] * n

def dfs(cur):
    visited[cur] = True
    for e in node[cur]:
        if visited[e]:
            continue
        dfs(e)


dfs(0)

cnt = sum(visited)
print(cnt)