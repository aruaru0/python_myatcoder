N, A, B = map(int, input().split())

# 高橋君のグリッドと青木君のグリッド
ga = [[0] * (N + 1) for _ in range(N + 1)]
gb = [[0] * (N + 1) for _ in range(N + 1)]

# 高橋君の広告を処理
for _ in range(A):
    r1, c1, r2, c2 = map(int, input().split())
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            ga[r][c] = 1
            
# 青木君の広告を処理
for _ in range(B):
    r1, c1, r2, c2 = map(int, input().split())
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            gb[r][c] = 1


# for i in range(N) :
#     print(ga[i])
# print("-----")
# for i in range(N) :
#     print(gb[i])

# 重なりを計算
res = 0
for r in range(1, N + 1):
    for c in range(1, N + 1):
        if ga[r][c] and gb[r][c]:
            res += 1
print(res)

