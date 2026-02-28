n, k = map(int, input().split())

cnt = 0
for _ in range(n) :
    a,b= map(int, input().split())
    if a*b >= k : cnt+=1

print(cnt)