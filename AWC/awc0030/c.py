n, k = map(int,input().split())
s = list(map(int, input().split()))
s.append(0)

cnt = 0
ans = 0
for e in s:
    if e == 1 :
        cnt+=1
    else:
        if cnt >= k : ans+=1
        cnt = 0

print(ans)