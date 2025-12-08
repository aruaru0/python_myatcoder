n = int(input())
a = list(map(int, input().split()))

cur = 0
for i in range(n) :
    if i > cur :
        break
    cur = max(cur, i+a[i]-1)

ans = min(n, cur+1)
print(ans)