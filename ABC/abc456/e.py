import sys
from collections import deque

def solve():
    ans = []
    
    N, M = map(int, input().split())

    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        
    W = int(input())
    
    S = []
    for i in range(N):
        S.append(input())
        
    # state: city * W + day
    is_v = [False] * ((N + 1) * W)
    v_cnt = 0
    for i in range(1, N + 1):
        s_i = S[i-1]
        for j in range(W):
            if s_i[j] == 'o':
                is_v[i * W + j] = True
                v_cnt += 1
    
    rev = [[] for _ in range((N + 1) * W)]
    deg = [0] * ((N + 1) * W)
    
    for i in range(1, N + 1):
        s_i = S[i-1]
        for j in range(W):
            if s_i[j] == 'o':
                curr = i * W + j
                nxt_d = (j + 1) % W
                
                # Check self
                nxt_s = i * W + nxt_d
                if is_v[nxt_s]:
                    deg[curr] += 1
                    rev[nxt_s].append(curr)
                
                # Check neighbors
                for nb in adj[i]:
                    nxt_n = nb * W + nxt_d
                    if is_v[nxt_n]:
                        deg[curr] += 1
                        rev[nxt_n].append(curr)

    q = deque()
    for i in range(1, N + 1):
        for j in range(W):
            st = i * W + j
            if is_v[st] and deg[st] == 0:
                q.append(st)
    
    rem = 0
    while q:
        u = q.popleft()
        rem += 1
        for v in rev[u]:
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    
    if rem < v_cnt:
        print("Yes")
    else:
        print("No")


t = int(input())
for _ in range(t) :
    solve()
