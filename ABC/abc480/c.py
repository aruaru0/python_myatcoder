n, k, t = map(int, input().split())
a = sorted(map(int, input().split()))

ans = 0
pos = 0 
i = 0
while pos < t:
    while i < n and a[i] <= pos:
        if a[i] + k > pos:
            pos = a[i] + k
        i += 1
    if pos >= t:
        break
    tg = a[i] if (i < n and a[i] <= t) else t
    m = (tg - pos + k - 1) // k
    ans += m
    pos += m * k

print(ans)
