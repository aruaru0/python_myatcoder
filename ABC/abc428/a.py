s, a, b, x = map(int, input().split())

cycle_len = a + b  
cyc = x // cycle_len 
ans = cyc * s * a 

rem = x % cycle_len 
run = min(rem, a)
ans += run * s
print(ans)
