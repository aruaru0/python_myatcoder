n = int(input())
a = list(map(int, input().split()))

ma = max(a)
cnt = 0
for e in a :
    if e == ma :
        cnt+=1


if cnt != 1 :
    print(0)
else :
    print(ma)