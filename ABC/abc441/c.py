n,k,x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

ans = n-k
cur = k-1

while(x > 0 and cur >= 0):
    x -= a[cur]
    ans += 1
    cur -= 1

if(x > 0):
    print(-1)
else:
    print(ans)