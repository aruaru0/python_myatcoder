N, X, Y = map(int, input().split())

X = abs(X)
Y = abs(Y)

ok = True
if X + Y > N : ok = False
if (X+Y)%2 != N%2 : ok = False

if ok :
    print("Yes")
else :
    print("No")