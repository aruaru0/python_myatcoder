n, q = map(int, input().split())

m = [(y, p) for y, p in [list(map(int, input().split())) for _ in range(n)]]
query = [(l, i) for i, l in enumerate([int(input()) for _ in range(q)])]

m.sort(reverse=True)
query.sort(reverse=True)

idx, sum = 0,0
ans = [0] * q
for (l, i) in query:
    while idx < n and m[idx][0] >= l :
        sum += m[idx][1]
        idx += 1

    ans[i] = sum


print(*ans, sep="\n")