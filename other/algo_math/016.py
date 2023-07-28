N = int(input())
a = list(map(int, input().split()))

def gcd(a:int, b:int) -> int:
    if b == 0 : return a
    return gcd(b, a%b)

def lcm(a:int, b:int) -> int:
    return a//gcd(a,b)*b


ans = a[0]
for e in a:
    ans = lcm(ans, e)

print(ans)