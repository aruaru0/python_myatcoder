n, m = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))

c.sort()
r.sort()

i = 0
cnt = 0
for e in c:
    while(i < m and r[i] < e) :
        i+=1

    if i == m :
        break

    cnt+=1
    i+=1

print(cnt)