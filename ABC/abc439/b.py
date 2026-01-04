n = int(input())

m = set()

while n not in m:
    m.add(n)
    x = 0
    while n > 0 :
        x += (n%10)**2
        n //= 10
    n = x

if n == 1:
    print("Yes")
else:
    print("No")