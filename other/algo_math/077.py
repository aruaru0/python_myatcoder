N = int(input())
x, y = [],[]
for i in range(N):
    xx, yy = map(int, input().split())
    x.append(xx)
    y.append(yy)


x.sort()
y.sort()

def calc(a) :
    n = len(a)
    b = [0 for _ in range (n+1)]
    for i in range(n):
        b[i+1] = b[i] + a[i]

    ret = 0
    for i in range(n):
        diff = b[n] - b[i+1] - a[i]*(n-1-i)
        ret += diff

    return ret


print(calc(x)+calc(y))
