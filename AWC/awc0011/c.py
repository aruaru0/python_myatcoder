n, k = map(int, input().split())
a = list(map(int, input().split()))
m = ~k  # Kにないビット
or_all = 0
cnt = 0
for v in a:
    if v & m == 0:  # 余計なビットがない
        cnt += 1
        or_all |= v
if cnt == 0 or or_all != k:
    print(-1)
else:
    print(cnt)