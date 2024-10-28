from bisect import bisect_left

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
V = K - sum(A)

if M == N:
    print(*[0 for _ in range(N)])
    exit()

a = [(A[i], i) for i in range(N)]
a.sort()
s = [0] * (N + 1)
for i in range(N):
    s[i + 1] = s[i] + a[i][0]
ans = [0] * N


def extra_votes(l, r, x):
    pos = bisect_left(a, (x, -1), lo=l, hi=r)
    # print(pos, a, l, r, x)
    return (pos - l) * x - (s[pos] - s[l])


for i in range(N):
    ng, ok = -1, V + 1
    while ng + 1 < ok:
        mi = (ng + ok) // 2
        x = a[i][0] + mi + 1
        if i < N - M:
            v = extra_votes(N - M, N, x)
            print("1:", v)
        else:
            v = (i - (N - M - 1)) * x - (s[i] - s[N - M - 1])
            v += extra_votes(i + 1, N, x)
            print("2:", v)

        if v > V - mi:
            ok = mi
        else:
            ng = mi
    print(ok)
    ans[a[i][1]] = ok if ok <= V else -1
print(*ans)
