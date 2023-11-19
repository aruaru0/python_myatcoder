n, m = map(int, input().split())


if n == 1:
    print('o'*m)
    exit()

v = n
K = 0
while v*n <= 1e9 :
    K+=1
    v*=n

ans = ""
for k in range(m):
    if  k <= K :
        ans += 'o'
    else:
        ans += 'x'

print(ans)