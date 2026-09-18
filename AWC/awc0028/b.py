n, l, r = map(int, input().split())
t = list(map(int, input().split()))


ans, cnt = 0,0
for e in t:
    if l <= e <= r :
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0


print(ans)