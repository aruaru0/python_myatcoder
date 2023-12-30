N = int(input())
p = list(map(int, input().split()))

q = [0 for _ in range(N)]
for i, e in enumerate(p):
    q[e-1] = i + 1 

print(*q)