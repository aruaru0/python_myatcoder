
n,m = map(int, input().split())
a = list(map(int, input().split()))

n2 = 1 << n

sum_val = [0] * n2
for i in range(n):
    shift_i = 1 << i
    val = a[i]
    for j in range(shift_i):
        sum_val[j | shift_i] = sum_val[j] + val

w = sum_val[n2 - 1] // m

dp = [0] * n2
for s in range(n2):
    dp_s = dp[s]
    for i in range(n):
        if not (s >> i & 1):
            ns = s | (1 << i)
            val = dp_s + (1 if sum_val[ns] % w == 0 else 0)
            if val > dp[ns]:
                dp[ns] = val

print(m - dp[n2 - 1])
