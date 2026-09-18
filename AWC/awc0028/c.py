n = int(input())
p = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

tot = sum(a) - sum(b)

ans = tot
for i in range(n):
    d = p[i] - b[i] - (a[i] - b[i])
    ans = max(ans, tot+d)

print(ans)