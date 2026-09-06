n = int(input())
x = list(map(int, input().split()))
x.sort()

k = 0
for i in range(n-1):
    k = max(k, x[i+1]-x[i])

print(k)