n, m = map(int, input().split())

a = list(map(int, input().split()))


cur = 0
p = [0] * n
for i in range (m) :
    x = a[i]-1
    p[x] += 1
    if p[x] > p[cur]:
        cur = x
    elif p[x] == p[cur] and x < cur :
        cur = x
    print(cur+1)