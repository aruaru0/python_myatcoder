N = int(input())


ans = 10**18
for i in range(1, N+1):
    if i*i > N : break
    if N%i == 0 :
        ans = min(ans, i+N//i)

print(ans*2)