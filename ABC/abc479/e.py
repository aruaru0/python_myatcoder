n = int(input())
m = n - 1
adj = [[] for _ in range(n + 1)]
ea = [0] * (m + 1)
eb = [0] * (m + 1)
for i in range(1, m + 1):
    a, b = map(int, input().split())
    ea[i] = a
    eb[i] = b
    adj[a].append((b, i))
    adj[b].append((a, i))

par = [0] * (n + 1)
order = []
st = [1]
par[1] = -1
while st:
    v = st.pop()
    order.append(v)
    for w, e in adj[v]:
        if w != par[v]:
            par[w] = v
            st.append(w)

sz = [1] * (n + 1)
for v in reversed(order):
    if par[v] > 0:
        sz[par[v]] += sz[v]

pos = [0] * (n + 1)
for idx, v in enumerate(order):
    pos[v] = idx

df = [0] * (n + 2)
gl = 0
for i in range(1, m + 1):
    a = ea[i]
    b = eb[i]
    c = a if par[a] == b else b 
    s = sz[c]
    l = pos[c]
    r = l + s
    if 2 * s > n:
        df[l] += i
        df[r] -= i
    else: 
        gl += i
        df[l] -= i
        df[r] += i

ans = [0] * (n + 1)
cur = 0
for idx in range(n):
    cur += df[idx]
    ans[order[idx]] = gl + cur

print(*ans[1:])
