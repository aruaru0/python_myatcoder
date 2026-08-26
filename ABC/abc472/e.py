import sys
from collections import deque

sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

def solve() :
    n, m = map(int, input().split())
    node = [[] for _ in range(n)]

    for _ in range(m) :
        u, v = map(int, input().split())
        u -=1
        v -=1
        node[u].append(v)
        node[v].append(u)

    col = [-1] * n
    vlist = deque()

    def dfs(cur, c) :
        nonlocal vlist
        if col[cur] != -1 :
            if col[cur] != c :
                while vlist[0] != cur :
                    vlist.popleft()
                return True
            return False

        vlist.append(cur)
        col[cur] = c
        for nxt in node[cur] :
            if dfs(nxt, 1-c) :
                return True

        vlist.pop()
        return False

    dfs(0,0)
    if len(vlist) != 0 :
        print(len(vlist))
        vlist = [e+1 for e in vlist]
        print(*vlist)
    else :
        print(-1)



T = int(input())
for _ in range(T) :
    solve()

