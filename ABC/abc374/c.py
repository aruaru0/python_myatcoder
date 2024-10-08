n = int(input())
k = list(map(int, input().split()))
ans = sum(k)

for bit in range(1 << n) :
    a, b = 0,0
    for i in range (n):
        if (bit>>i)%2 :
            a += k[i]
        else :
            b += k[i]

    ans = min(ans, max(a,b))

print(ans)