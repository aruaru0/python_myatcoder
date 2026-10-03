from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))


max_v = max(a)

cnt = [0] * (max_v + 1)
for x in a:
    cnt[x] += 1


ans = 0
for d in range(1, max_v + 1):
    count = 0 
    for i in range(d, max_v + 1, d):
        count += cnt[i]    

    val = d * count
    if val > ans:
        ans = val

print(ans)
