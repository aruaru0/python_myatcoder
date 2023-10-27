n = int(input())

mod = 10**9 + 7
sum = n*(n+1)//2
sum %= mod

ans = sum * sum %mod

print(ans)