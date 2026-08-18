import heapq

q, v = map(int, input().split())
h = []  # 最大ヒープ: -(w - t) を格納
ans = []
for _ in range(q):
    s = input().split()
    if s[0] == '1':
        t = int(s[1])
        w = int(s[2])
        heapq.heappush(h, t - w)  # key = w - t のマイナス
    else:
        t = int(s[1])
        if not h:
            ans.append('-1')
        else:
            k = -heapq.heappop(h)  # 最大の key = w - t
            ans.append(str(min(v, k + t)))
print('\n'.join(ans))