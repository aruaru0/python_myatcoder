n = int(input())
a = list(map(int, input().split()))

x1, x10, x100 = 0,0,0
for e in a :
    d = (e+999)//1000*1000 - e
    x1 += d%10
    x10 += d//10 %10
    x100 += d//100 %10

print(x1, x10, x100)
