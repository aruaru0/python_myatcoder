import sys
sys.setrecursionlimit(10**6)

n = int(input())
t = [e-1 for e in map(int, input().split())]

dist = [-1]*n
used = [False]*n
m = {}

def dfs(cur, cnt) :
    if used[cur] :
        if dist[cur] != -1 :
            return dist[cur]
        return cnt - m[cur]

    m[cur] = cnt
    used[cur] = True
    ret = dfs(t[cur], cnt+1)
    dist[cur] = ret
    return ret

for i in range(n) :
    if not used[i] :
        dfs(i, 0)

print(*dist)
