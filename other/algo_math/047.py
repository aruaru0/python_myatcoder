import sys
sys.setrecursionlimit(10 ** 6)


N, M = map(int, input().split())
node = [[] for _ in range (N)]

for _ in range(M) :
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node[a].append(b)
    node[b].append(a)


color = [0] * N

def dfs(cur, col) :
    color[cur] = col
    for e in node[cur]:
        if color[e] == col : 
            return False
        if color[e] != 0 : 
            continue
        if dfs(e, -col) == False : return False

    return True

for i in range(N):
    if color[i] == 0 and dfs(i, 1) == False :
        print("No")
        exit()

print("Yes")
    


