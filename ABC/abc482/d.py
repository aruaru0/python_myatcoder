N = int(input())
X = list(map(int, input().split()))

ans = []
for k in range(N):
    if N == 1:
        ans.append(0)
        continue
    best = 10**18
    # 先に右隣 k+1 と出会い、そこから左へ1体を送る
    if k + 1 < N:
        t = max((X[-1] - X[k]) // 2, (X[k + 1] - X[0]) // 2)
        if t < best:
            best = t
    # 先に左隣 k-1 と出会い、そこから右へ1体を送る
    if k - 1 >= 0:
        t = max((X[-1] - X[k - 1]) // 2, (X[k] - X[0]) // 2)
        if t < best:
            best = t
    ans.append(best)

print('\n'.join(map(str, ans)))
