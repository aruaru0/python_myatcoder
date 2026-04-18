import sys

n,m = map(int, input().split())
f = [0]*n
d = [0]*n
for i in range(n):
    f[i], d[i] = map(int, input().split())

# 二分探索: 収穫量が X 以上となる回数の合計が M 回以下となる最小の X を探す。
# X が大きいほど、回数は少なくなる。
low = 1
high = 10**9 + 7
ans_x = high

while low <= high:
    mid = (low + high) // 2
    cnt = 0
    for i in range(n):
        if f[i] >= mid:
            # F_i - (k-1)D_i >= mid  => k-1 <= (F_i - mid)//D_i
            num = (f[i] - mid) // d[i] + 1
            cnt += num
    if cnt <= m:
        ans_x = mid
        high = mid - 1
    else:
        low = mid + 1

# ans_x 以上をすべて足す。この回数は必ず M 回以下。
res = 0
cnt = 0
for i in range(n):
    if f[i] >= ans_x:
        num = (f[i] - ans_x) // d[i] + 1
        last = f[i] - (num - 1) * d[i]
        res += num * (f[i] + last) // 2
        cnt += num

# 残りの回数分は、ans_x 未満の最大値である ans_x - 1 を足す。
rem = m - cnt
if rem > 0:
    val = ans_x - 1
    if val < 0:
        val = 0
    res += rem * val

print(res)

