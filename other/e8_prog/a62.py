import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

node = [[] for _ in range(N)]
for _ in range(M) :
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node[a].append(b)
    node[b].append(a)


def dfs(cur) :
    used[cur] = True
    for e in node[cur]:
        if used[e] == False :
            dfs(e)

used = [False for _ in range(N)]
dfs(0)

if sum(used) == N :
    print("The graph is connected.")
else:
    print("The graph is not connected.")
