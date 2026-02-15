n, m, k = map(int, input().split())

a = list(map(int, input().split()))
b = set(map(int, input().split()))

tot, cnt = 0,0
for i in range(n) :
    if a[i] < k and i+1 in b :
        cnt+=1
        tot+=a[i]


print(cnt, tot)