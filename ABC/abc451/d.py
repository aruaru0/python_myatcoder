import heapq

N = int(input())
parts = []
k = 0
while True:
    val = 1 << k
    if val > 1e9:
        break
    s_val = str(val)
    parts.append(s_val)
    k += 1

parts_len = [len(p) for p in parts]


heap = [int(p) for p in parts]
heapq.heapify(heap)


count = 0
last_popped = -1  # 前回取り出した値を記録する変数

ans = 0
while True:
    x = heapq.heappop(heap)
    
    # 重複排除：前回と同じ値ならスキップ
    if x == last_popped:
        continue
    last_popped = x
    
    count += 1
    if count == N:
        ans = x
        break
    
    x_str = str(x)
    len_x = len(x_str)
    for i in range(len(parts)):
        s = parts[i]
        if len_x + parts_len[i] > 10:
            continue
        new_val = int(x_str + s)
        if new_val <= 1e9:
            heapq.heappush(heap, new_val)

print(ans)