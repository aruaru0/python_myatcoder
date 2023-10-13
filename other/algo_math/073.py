n = int(input())
a = list(map(int, input().split()))

x = 1
ans = 0
mod = 10**9 + 7
for e in a :
    ans = (ans + x*e%mod) %mod
    x = x*2 % mod

print(ans)
