import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
adj = []
for _ in range(N):
    parts = list(map(int, input().split()))
    adj.append([x - 1 for x in parts[1:]])

match = [-1] * M  # match[c] = 時間帯cが割り当てられている時間帯のindex
# print(adj)

def dfs(u, vis):
    for v in adj[u]:
        if not vis[v]:
            vis[v] = True
            if match[v] < 0 or dfs(match[v], vis):
                match[v] = u
                return True
    return False

ans = 0
for i in range(N):
    vis = [False] * M
    if dfs(i, vis):
        ans += 1
print(ans)

