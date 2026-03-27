N, K = map(int, input().split())
A = list(map(int, input().split()))

total_sum = sum(A)

l = 1
r = total_sum
ans = 0

while l <= r:
    m = (l + r) // 2
    
    cnt = 0
    current_s = 0

    for w in A:
        current_s += w
        if current_s >= m:
            cnt += 1
            current_s = 0
            
    if cnt >= K:
        ans = m
        l = m + 1
    else:
        r = m - 1

print(ans)
