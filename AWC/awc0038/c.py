n, l, k = map(int, input().split())
a = list(map(int, input().split()))

if sum(a) <= l and n <= k+1 :
    print(n)
    exit()

a.sort()

tot, cnt = 0,0
for i in range(n) :
    tot += a[i]
    if i > k :
        break
    if tot <= l :
        cnt += 1

print(cnt)