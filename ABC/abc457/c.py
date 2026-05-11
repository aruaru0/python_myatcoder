
N, K = map(int, input().split())

A_list = []
L_list = []

for _ in range(N):
    input_data = list(map(int, input().split()))
    L_i = int(input_data[0])
    A_i = input_data[1:]
    A_list.append(A_i)
    L_list.append(L_i)
    
C_list = list(map(int, input().split()))
    
current_total = 0

for i in range(N):
    L_i = L_list[i]
    C_i = C_list[i]
    block_size = L_i * C_i
    
    # K がこのブロックの範囲内にあるか判定
    if K <= current_total + block_size:
        # ブロック内の相対的なインデックスを計算 (0-indexed)
        # (K - current_total - 1) は、現在のブロックの開始位置からのオフセット
        target_idx = (K - current_total - 1) % L_i
        print(A_list[i][target_idx])
        exit()

    # 次のブロックへ
    current_total += block_size

