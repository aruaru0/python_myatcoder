from functools import lru_cache
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

@lru_cache(maxsize=None)
def dfs(cur, cnt) :
    global K, node
    
    if cnt == 2*K :
        if s[cur] == 'A' : return True
        return False
    
    r = set()
    for e in  node[cur] :
        r.add(dfs(e, cnt+1))

    if cnt % 2 == 0 : # Aliceのターン
        if True in r:
            return True
        return False
    else : # Bobのターン
        if False in r:
            return False
        return True


T = int(input()) 

for _ in range(T) :
    N, M, K = map(int, input().split())
    s = input()
    node = [[] for _ in range(N)]

    for _ in range(M) :
        u, v = map(int, input().split())
        u-=1
        v-=1
        node[u].append(v)

    if dfs(0, 0) :
        print("Alice")
    else :
        print("Bob")
    
    dfs.cache_clear()

    