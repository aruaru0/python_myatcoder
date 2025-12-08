import sys


#再帰の深さ設定
sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline


n, m = map(int, input().split())

node = [[] for _ in range (n)]
for _ in range(m) :
    x, y = map(int, input().split())
    x-=1
    y-=1
    node[y].append(x)

ok = [False]*n

def dfs(cur:int) :
    if ok[cur] : return
    ok[cur] = True
    for e in node[cur]:
        dfs(e)
    

q = int(input())
for _ in range(q) :
    t, v = map(int, input().split())
    v -= 1
    if t == 1 :
        dfs(v)
    else :
        if ok[v] :
            print('Yes')
        else :
            print('No')