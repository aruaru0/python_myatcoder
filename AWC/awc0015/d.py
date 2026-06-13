n, m, c = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

j = 0
cnt = 0
for i in range(n) :
    if j < m and a[i] >= b[j] :
        j+=1
        cnt+=1

print(cnt*c)
    