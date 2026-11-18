n, L, R = map(int, input().split())
a = list(map(int, input().split()))

# 累積和 p[0..n]
p = [0] * (n + 1)
s = 0
for i in range(n):
    s += a[i]
    p[i + 1] = s

# マージソートの各段で「左半分の添字 < 右半分の添字」の組を数える
# 部分列和 = p[j] - p[i] (i < j) なので L <= p[j] - p[i] <= R を数える
ln = n + 1
w = p
ans = 0
wd = 1
while wd < ln:
    step = wd * 2
    for lo in range(0, ln, step):
        mid = lo + wd
        if mid >= ln:
            break
        hi = mid + wd
        if hi > ln:
            hi = ln
        q1 = lo
        q2 = lo
        for v in w[mid:hi]:
            b1 = v - R
            while q1 < mid and w[q1] < b1:
                q1 += 1
            b2 = v - L
            while q2 < mid and w[q2] <= b2:
                q2 += 1
            ans += q2 - q1
        # 両半分はソート済みなので sorted はそのままマージする
        w[lo:hi] = sorted(w[lo:hi])
    wd = step

print(ans)
