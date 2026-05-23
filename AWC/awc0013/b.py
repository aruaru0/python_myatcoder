N, M = map(int, input().split())
S = set()

for _ in range(M):
    u, v = map(int, input().split())
    S.add((u, v))

ans = 0
for u, v in S:
    if u < v and (v, u) in S:
        ans += 1

print(ans)
