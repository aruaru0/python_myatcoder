n = int(input())
l = list(map(int, input().split()))
sum1 = sum(l)

ans = sum1
sum2 = 0
for e in l:
    sum2 += e
    sum1 -= e
    ans = min(ans, abs(sum2-sum1))


print(ans)