n = int(input()) 

cnt, tot = 0,0
for _ in range(n) :
    a, b = map(int, input().split())
    if a > b :
        cnt += 1
        tot += a - b

print(cnt, tot)