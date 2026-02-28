n = int(input())

a = [input().split() for _ in range(n)]

cnt = 0
for i in range(n-1):
    if a[i][1] == a[i+1][0] : cnt+=1


print(cnt)