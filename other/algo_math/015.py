N = int(input())
a = list(map(int, input().split()))


def gcd(a:int, b:int) ->int  :
    if b == 0 : return a
    return gcd(b, a%b)


ans = a[0]
for e in a :
    ans = gcd(ans, e)

print(ans)