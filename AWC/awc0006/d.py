N, M = map(int, input().split())

I = []
for _ in range(M):
    L, R = map(int, input().split())
    I.append([L, R])

I.sort()

cur = 1
ans = 0
idx = 0

while cur <= N:
    best_r = -1
    
    while idx < M and I[idx][0] <= cur:
        if I[idx][1] > best_r:
            best_r = I[idx][1]
        idx += 1
    
    if best_r == -1 or best_r < cur:
        print(-1)
        exit()
    
    ans += 1
    
    if best_r >= N:
        break
    
    cur = best_r + 1

print(ans)
