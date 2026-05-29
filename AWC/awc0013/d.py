N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for k in range(M):
    c = [B[i][k] for i in range(N)]
    c.sort()
    for i in range(N):
        ans += (2 * i - N + 1) * c[i]

print(ans)
