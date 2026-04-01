N = int(input())

A = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N):
        dists = list(map(int, input().split()))
        for j, d in enumerate(dists, start=i + 1):
            A[i][j] = d
            A[j][i] = d

edges = []
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if A[i][j] <= 0:
            print("No")
            exit()
        edges.append((A[i][j], i, j))

edges.sort()

parent = list(range(N + 1))
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        parent[px] = py

adj = [[] for _ in range(N + 1)]
edge_count = 0

for dist, u, v in edges:
    pu, pv = find(u), find(v)
    if pu != pv:
        union(pu, pv)
        adj[u].append((v, dist))
        adj[v].append((u, dist))
        edge_count += 1

if edge_count < N - 1:
    print("No")
    exit()

def bfs(start):
    dist = [-1] * (N + 1)
    dist[start] = 0
    q = [start]
    
    idx = 0
    while idx < len(q):
        u = q[idx]
        idx += 1
        for v, w in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + w
                q.append(v)
    
    return dist

for i in range(1, N + 1):
    d = bfs(i)
    for j in range(i + 1, N + 1):
        if d[j] != A[i][j]:
            print("No")
            exit()

print("Yes")

