n = int(input())


mod = 10**9 + 7
ans = pow(4, n+1, mod)
ans -= 1
if ans < 0 : ans += mod
div3 = pow(3,  mod-2, mod)
ans = ans * div3 % mod
print(ans)