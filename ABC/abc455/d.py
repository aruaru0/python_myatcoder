N, Q = map(int, input().split())

up = [-1]*N
down = [-1]*N

for _ in range(Q):
    c, p = map(int, input().split())
    c-=1
    p-=1
    if down[c] != -1 :
        up[down[c]] = -1

    up[p] = c
    down[c] = p

ans = [0]*N
for i in range(N) :
    if down[i] == -1 :
        cur = i
        while cur != -1 :
            cur = up[cur]
            ans[i] += 1

print(*ans)
