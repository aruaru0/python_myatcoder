import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, graph):
    n = len(graph)
    dist = [-1] * n
    dist[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

def farthest_nodes(dist):
    """距離配列から最遠距離の頂点すべてを列挙し、その中で最大番号を返す"""
    maxd = max(dist)
    return max([i for i, d in enumerate(dist) if d == maxd])


N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    graph[a].append(b)
    graph[b].append(a)

# 1回目: 適当な頂点(0)から最遠点候補を求める
dist0 = bfs(0, graph)
A = farthest_nodes(dist0)

# 2回目: Aから最遠点候補を求める
distA = bfs(A, graph)
B = farthest_nodes(distA)

# 3回目: Bからの距離
distB = bfs(B, graph)

# 各頂点 v に対して答えを決める
out = []
for v in range(N):
    dA, dB = distA[v], distB[v]
    if dA > dB:
        out.append(str(A+1))
    elif dB > dA:
        out.append(str(B+1))
    else:
        out.append(str(max(A, B)+1))  # 同距離なら番号大きい方
print("\n".join(out))

