N = int(input())
M = 10 ** 6
a = [0] * M

for _ in range(N):
    s, v = input().split()
    a[int(s)] += int(v)

p = 1
for _ in range(6):
    for i in range(M):
        if i // p % 10 != 0:
            a[i] += a[i - p]
    p *= 10

Q = int(input())
out_lines = []
# dims[0]=一の位, dims[5]=十万の位
dims = [1, 10, 100, 1000, 10000, 100000]

for _ in range(Q):
    x, y = input().split()
    # yk[d]: d=0が一の位, y[5]が一の位
    yk = [int(y[5 - d]) for d in range(6)]
    xk = [int(x[5 - d]) for d in range(6)]

    empty = False
    for d in range(6):
        if xk[d] > yk[d]:
            empty = True
            break
    if empty:
        out_lines.append("0")
        continue

    ans = 0
    for mask in range(64):
        idx = 0
        sign = 1
        ok = True
        for d in range(6):
            if mask >> d & 1:
                v = xk[d] - 1
                if v < 0:
                    ok = False
                    break
                idx += v * dims[d]
                sign = -sign
            else:
                idx += yk[d] * dims[d]
        if ok:
            ans += a[idx] * sign
    out_lines.append(str(ans))

print("\n".join(out_lines))