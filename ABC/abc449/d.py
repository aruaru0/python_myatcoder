L, R, D, U = map(int, input().split())

# 最大絶対値。k>この値で g(k) は全点数になる。
K = max(abs(L), abs(R), abs(D), abs(U))

total_points = (R - L + 1) * (U - D + 1)

ans = 0
prev_g = 0

for k in range(K + 1):
    # x の有効範囲
    xl = max(L, -k)
    xr = min(R, k)
    if xl > xr:
        w = 0
    else:
        w = xr - xl + 1

    # y の有効範囲
    yl = max(D, -k)
    yu = min(U, k)
    if yl > yu:
        hgt = 0
    else:
        hgt = yu - yl + 1

    cur_g = w * hgt   # g(k)

    h_k = cur_g - prev_g   # max がちょうど k の点数
    if k % 2 == 0:         # 黒点
        ans += h_k

    prev_g = cur_g

print(ans)


