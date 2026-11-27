n = int(input())
h = list(map(int, input().split()))

cur, ans = 0,[]
for i in range(n) :
    if cur < h[i] :
        cur = h[i]
        ans.append(i+1)


print(*ans)