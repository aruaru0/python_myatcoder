n, q = map(int, input().split())
a = list(map(int, input().split()))

# prefix sum (pre[0]=0)
pre = [0] * (n + 1)
for i in range(n):
    pre[i + 1] = pre[i] + a[i]

off = 0               # 現在の先頭が元配列で何番目か（0-index）
out = []              # 出力を貯める

for _ in range(q):
    tmp = input().split()
    if tmp[0] == '1':                     # 回転クエリ
        c = int(tmp[1]) % n               # N で割った余りだけ残す
        off = (off + c) % n
    else:                                 # 区間和クエリ
        l = int(tmp[1])
        r = int(tmp[2])

        L = (off + l - 1) % n
        R = (off + r - 1) % n

        if L <= R:
            ans = pre[R + 1] - pre[L]
        else:
            ans = (pre[n] - pre[L]) + pre[R + 1]

        out.append(str(ans))

print('\n'.join(out))


