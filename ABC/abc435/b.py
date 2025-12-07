n = int(input())
a = list(map(int, input().split()))
b = [0 for _ in range(n+1)]
for i in range(n) :
    b[i+1] = b[i] + a[i]


ans = 0
for l in range(n) :
    for r in range(l, n) :
        sum = b[r+1] - b[l]
        ok = True
        for i in range(l, r+1) :
            if sum%a[i] == 0 :
                ok = False
                break
        if ok : ans += 1

print(ans)