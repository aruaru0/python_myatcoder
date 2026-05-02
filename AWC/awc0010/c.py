N, K, Q = map(int, input().split())
A = list(map(int, input().split()))

rend = [0] * N
rend[N - 1] = N - 1

for i in range(N - 2, -1, -1):
    if abs(A[i] - A[i + 1]) <= K:
        rend[i] = rend[i + 1]
    else:
        rend[i] = i

for _ in range(Q):
    L, R = map(int, input().split())
    li = L - 1
    ri = R - 1
    
    if rend[li] >= ri:
        print("Yes")
    else:
        print("No")
