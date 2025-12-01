n, m = map(int, input().split())

sum = [0]*m
cnt = [0]*m
for i in range(n) :
    a, b = map(int, input().split())
    a -= 1
    sum[a]+=b
    cnt[a]+=1


for i in range(m):
    print(sum[i]/cnt[i])