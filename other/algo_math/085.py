N, X, Y = map(int, input().split())

for a in range(1, N+1):
    for b in range(1, N+1):
        for c in range(1, N+1):
            d = X - a - b - c
            if 1 <= d and d <= N and Y==a*b*c*d :
                print("Yes")
                exit()

print("No")