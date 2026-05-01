N = int(input())
D = list(map(int, input().split()))

ans = D[0]
for i in range(1, N):
    if D[i-1] < D[i]:
        ans += D[i] // 2
    else:
        ans += D[i]

print(ans)
