n, m = map(int, input().split())
ed = []
for _ in range(m):
    u, v = map(int, input().split())
    ed.append((u - 1, v - 1))

ans = m  # 最大は全辺削除
for mask in range(1 << n):
    cnt = 0
    for (a, b) in ed:
        ca = (mask >> a) & 1
        cb = (mask >> b) & 1
        if ca == cb:      # 同側なら削除必須
            cnt += 1
    if cnt < ans:
        ans = cnt
print(ans)


