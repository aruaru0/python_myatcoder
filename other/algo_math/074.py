n = int(input())
a = list(map(int, input().split()))
b = [0 for _ in range(n+1)]
for i in range(n) :
    b[i+1] = b[i] + a[i]


ans = 0 
for i in range(n):
    tot = b[n] - b[i+1] - a[i] * (n-1-i)
    ans += tot

print(ans)