# 入力取得
N, M = map(int, input().split())

# 行ごとの出力
for i in range(1, N + 1):
    if i <= M:
        print("OK")
    else:
        print("Too Many Requests")
