import sys
sys.setrecursionlimit(10**6)

N = int(input())

node = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node[a].append(b)
    node[b].append(a)

used = [False for _ in range(N)]

def dfs(cur) :
    used[cur] = True
    for e in node[cur]:
        if used[e] : continue
        dfs(e)


dfs(0)

if sum(used) == N :
    print("Yes")
else :
    print("No")