n, k = map(int, input().split())

ok = [bytearray(k + 1) for _ in range(n + 1)]
ok[n][0] = 1
for i in range(n - 1, -1, -1):
    w = i + 1
    row = ok[i]
    row[:] = ok[i + 1]
    for s in range(w, k + 1):
        if row[s - w]:
            row[s] = 1

out = []
cur = [0] * n


def dfs(i, rem):
    if i == n - 1:
        if rem % n == 0:
            cur[i] = rem // n
            out.append(' '.join(map(str, cur)))
        return
    w = i + 1
    x = 0
    while x * w <= rem:
        t = rem - x * w
        if ok[i + 1][t]:
            cur[i] = x
            dfs(i + 1, t)
        x += 1


dfs(0, k)
print('\n'.join(out))