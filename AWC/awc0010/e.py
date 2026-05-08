from itertools import permutations 

n, k_limit = map(int, input().split())


c = [list(map(int, input().split())) for _ in range(n)]

initial = list(range(n))

max_effect = 0

for p in permutations(range(n)):
    visited = [False] * n
    cycles = 0
    for i in range(n):
        if not visited[i]:
            cycles += 1
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = p[curr]
    
    min_swaps = n - cycles
    
    if min_swaps <= k_limit:
        current_effect = 0
        for i in range(n):
            u = p[i]
            v = p[(i + 1) % n]
            current_effect += c[u][v]
        
        if current_effect > max_effect:
            max_effect = current_effect

print(max_effect)

