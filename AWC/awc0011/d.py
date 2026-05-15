import sys

sys.setrecursionlimit(10**6)


N, Q = map(int, input().split())
V = list(map(int, input().split()))
P = list(map(int, input().split()))
node = [[] for _ in range(N)]
for i, e in enumerate(P):
    node[e-1].append(i+1)

money = [0]*N

def dfs(cur, cost) :
    money[cur] = cost + V[cur]
    for e in node[cur] :
        dfs(e, money[cur])

dfs(0,0)

for _ in range(Q):
    x = int(input())-1
    print(money[x])