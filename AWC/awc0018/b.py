from collections import defaultdict

n, m = map(int, input().split())
c = list(map(int, input().split()))

ans = 0
for _ in range(n):
    k = int(input())
    p = list(map(int, input().split()))
    cnt = defaultdict(int)
    for e in p:
        cnt[e-1] += 1
    for idx, num in cnt.items() :
        if c[idx] >= num :
            ans += num

print(ans)