N, M = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)

if S >= M:
    print("Yes")
else:
    print("No")
