import collections

# 入力は input() を用いる
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

s = input().strip()

INF = 10 ** 9
d1 = [INF] * n          # 最短距離
d2 = [INF] * n          # 2 番目の距離
p1 = [-1] * n           # そのときの起点安全頂点
p2 = [-1] * n

q = collections.deque()
for i, ch in enumerate(s):
    if ch == 'S':
        d1[i] = 0
        p1[i] = i
        q.append((i, i))          # (現在地, 起点)

while q:
    v, src = q.popleft()
    cur = d1[v] if src == p1[v] else d2[v]
    for w in g[v]:
        nd = cur + 1
        if src == p1[w]:
            if nd < d1[w]:
                d1[w] = nd
                q.append((w, src))
        elif src == p2[w]:
            if nd < d2[w]:
                d2[w] = nd
                q.append((w, src))
        else:
            if nd < d1[w]:
                # 今の最短を 2 番目にずらす
                d2[w], p2[w] = d1[w], p1[w]
                d1[w], p1[w] = nd, src
                q.append((w, src))
            elif nd < d2[w]:
                d2[w], p2[w] = nd, src
                q.append((w, src))

out = []
for i, ch in enumerate(s):
    if ch == 'D':
        out.append(str(d1[i] + d2[i]))
print("\n".join(out))


