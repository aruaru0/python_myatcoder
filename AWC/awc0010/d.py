N, K = map(int, input().split())
H = list(map(int, input().split()))

H.sort(reverse=True)

ans = sum(H)

for i in range(K):
    ans -= (H[i] - 1)

print(ans)
