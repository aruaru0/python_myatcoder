N = int(input())

ans = []

i = 2
while i*i <= N :
    while N%i == 0 :
        ans.append(i)
        N //= i
    i += 1

if N >= 2 :
    ans.append(N)

print(*ans)