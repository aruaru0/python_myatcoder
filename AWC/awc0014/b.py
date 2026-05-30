N, V = map(int, input().split())
D = list(map(int, input().split()))
T = list(map(int, input().split()))

ans = []
dist = 0
for i in range(N - 1):
    dist += D[i]
    if dist < T[i] * V:
        ans.append(i + 2)

if not ans:
    print("-1")
else:
    print(*ans)
