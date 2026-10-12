n, w = map(int, input().split())

ab = [list(map(int, input().split())) for _ in range(n)]


ans = 0
for bit in range(1<<n) :
    sumA, sumB = 0,0
    for i in range(n):
        if bit>>i & 1 :
            sumA += ab[i][0]
            sumB += ab[i][1]


    if sumB <= w :
        ans = max(ans, sumA)

print(ans)