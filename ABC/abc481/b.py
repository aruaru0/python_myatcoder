n, k = map(int, input().split())
a = list(map(int, input().split()))


cur = a[0]
cnt = 0 if cur != k else 1

for e in a[1:] :
    if e == k : cnt += 1
    elif cur < k and e > k : cnt += 1
    elif cur > k and e < k : cnt += 1
    cur = e

print(cnt)