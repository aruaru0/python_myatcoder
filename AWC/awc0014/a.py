N, R, T = map(int, input().split())
P = list(map(int, input().split()))

ans = []
for p in P:
    ans.append(min(R, T // p))

print(*ans)
