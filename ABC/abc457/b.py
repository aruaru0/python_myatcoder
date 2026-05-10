N = int(input())

A = []

for _ in range(N):
    s = list(map(int, input().split()))

    A.append(s[1:])    

X, Y = map(int, input().split())

print(A[X - 1][Y - 1])
