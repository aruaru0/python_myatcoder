import sys
from collections import defaultdict

sys.setrecursionlimit(300000)

N = int(input())

# A_i は0インデックスで扱うためにリスト化
A = list(map(int, input().split()))

adj = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u-=1   
    v-=1
    adj[u].append(v)
    adj[v].append(u)
    
ok = [False] * N
cnt = defaultdict(int)

def dfs(cur, prev):
    val = A[cur]
    cnt[val] += 1
    
    if (prev != -1 and ok[prev]) or cnt[val] >= 2:
        ok[cur] = True
        
    for nxt in adj[cur]:
        if nxt == prev:
            continue
        dfs(nxt, cur)
        
    cnt[val] -= 1

dfs(0, -1)

ans = []
for is_ok in ok:
    if is_ok:
        ans.append("Yes")
    else:
        ans.append("No")
        
print('\n'.join(ans))
